# Legacy closed-loop rollout

This loop remains for historical reproduction. The current V1
planner-specific parser, safe-bin quantization, continuous capture and exact
robot payload flow are documented in [`planner_benchmark/README.md`](https://github.com/CoNG-harvard/unidog_nav/blob/main/planner_benchmark/README.md#live-planner-to-robot-data-flow).

`scripts/rollout.py` is **event-driven, not fixed-frequency**: each cycle
blocks until the robot finishes moving. One cycle ("planning step") =

1. fetch a fresh frame from the robot (`GET /image`, ~1.4 s) — saved as `step_NNN.jpg`
2. build the 8-frame model input (faithful port of the official `sample_and_pad_images`: black-pad at episode start, then uniform sample + latest frame)
3. planner predicts **one discrete action** as text (~0.6 s for NaVILA)
4. `navigation_policy.navila_parser` parses/validates it into a skill plan
5. `POST /plan` — the robot executes and the loop waits (currently ~13–22 s, setup-dominated)
6. repeat until the planner says stop, a failure aborts, or `--max-steps`.

NaVILA emits exactly one action per cycle by design (its trained action space: turn 15/30/45°, move 25/50/75 cm, stop) — execute-one-then-replan is what makes the loop self-correcting. A plan can still contain several calls: the episode's first motion plan gets the `stand` + `check_robot_ready` prologue, and a `move forward > 2 m` is chunked into multiple `move_forward` calls; all calls of one plan run in a single `run_plan.py` subprocess without replanning between them.

Example trace (real episode, 2026-07-12, instruction *"Move forward, when seeing the orange chair, turn right and stop."*):

| cycle | robot saw (`step_N.jpg`) | model output | executed |
|---|---|---|---|
| 0 | path ahead blocked, orange chair far left | `turn left 45 degree` | stand + ready check + turn +45° |
| 1 | (new heading) | `turn left 45 degree` | turn +45° |
| 2 | open path | `move forward 75 cm` | forward 0.75 m |
| 3–6 | chair passing to the right | `turn right 45/45/15/45` | turns −150° total |
| 7 | chair no longer visible | "I think I should stop…" | stop → episode ends |

## Running a real-robot rollout (full command log)

```bash
# [workstation] 1. read-only preflight: verifies SSH, deployed entry points,
# robot branch offline-rl-vlm-policy, and a clean robot worktree
bash scripts/prepare_real_robot.sh --check

# [workstation] 2. interactively confirm, start REAL mode, open/reuse the tunnel,
# and verify health (type the exact confirmation requested by the script)
bash scripts/prepare_real_robot.sh

# [workstation] 3. optional independent recheck:
# expect backend "run_plan.py (batch)" and real: true
python3 scripts/robot_client.py health

# [workstation] 4. run the rollout (NaVILA planner; GPU must be free of the Qwen server)
conda activate navila
python scripts/rollout.py --planner navila --max-steps 10 --continue-on-failure \
    --tag my-test --instruction "Turn right and walk to the orange chair. Stop in front of it."

# Qwen3-VL as planner instead: start agent_ai/start_vllm.sh first (GPU-exclusive with NaVILA)
python scripts/rollout.py --planner qwen --instruction "..."
```

## V1 structured Qwen live skill-interface test

The older `scripts/rollout.py --planner qwen` path above keeps the legacy
25/50/75 cm free-text action vocabulary. To test the V1 JSON interface,
semantic `speed_level`, safe-bin quantization, F3 image history, executed
action history, operator gate, and robot execution together, use:

```bash
conda run -n navila python -m planner_benchmark.run_live \
  --scenario L1-QWEN-V1-NORMAL-1M \
  --planner qwen \
  --repeats 1 \
  --acting-policy F3 \
  --operator <name>
```

Run `L1-QWEN-V1-FAST-1M` only after the normal-speed trial passes in a
measured clear lane. Legacy scenarios retain their fixed-increment
`normalization:` for historical comparability and must be run with the explicit
`--normalize` compatibility flag. V1 scenarios use `quantization:`
and log the untouched proposal, executable action, and every transform record.

`--continue-on-failure` is recommended: a partially completed skill (e.g. a small turn hitting its backstop) replans from the next frame instead of ending the episode (3 consecutive failures still abort). Emergency stop at any time: Ctrl-C (aborts the skill and stops the robot) or `python3 scripts/robot_client.py stop`.

## Where the results are

One folder per episode: `logs/rollouts/<planner>_<tag>_t<timestamp>/` (tag defaults to the slugified instruction; set `--tag` for a readable name).

- `step_NNN.jpg` — the exact frame the planner saw at cycle N. **#frames = #planning steps.**
- `episode.json` — per step: raw model output, parsed plan, full per-skill `SkillResult`s (measured progress, safety status), `planner_sec`/`robot_sec`, and the batch runner's `timing.setup_s`. Episode `status`: `stopped_by_planner` (planner said stop), `max_steps_reached`, `skill_failed`, `parse_error`, `robot_error`, `interrupted`.

## Recommended instructions (NaVILA)

NaVILA is a trained VLN policy, not a literal command interpreter: it treats the instruction as a goal description and picks actions from instruction + current view. Phrase like R2R training data:

- Good: `"Turn right and walk to the orange chair. Stop in front of it."` / `"Walk straight ahead. Turn right at the orange chair. Stop."` — explicit direction words, sequential clauses.
- Avoid: conditionals ("when seeing X, do Y"), literal angles ("turn right 15 degrees" — it turns until the goal looks right, not by your number), and fine-grained qualifiers ("at a safe distance", "the rightmost").
- Start pose matters: if the path ahead is blocked, the policy will turn regardless of what the instruction says first. If the goal object is not in view at all, it explores.
- In `scripts/rollout.py`, `--planner qwen` follows literal clauses better than NaVILA. In `planner_benchmark.run_live`, the same `qwen` planner uses the V1 structured interface by default; add `--normalize` only to reproduce the old benchmark contract.

Within legacy `scripts/rollout.py`, both planners emit the same discrete action grammar. Its Qwen regex constraint is separate from the V1 JSON-schema constraint used by the default live-benchmark Qwen path.

Verified: mock loop 2026-07-11 (both planners); real robot 2026-07-12 (NaVILA, guarded motion). Note for launching the Qwen server from wrapper environments: `agent_ai/start_vllm.sh` pins `CC`/`CXX`/`PATH`/`LIBRARY_PATH` because triton/flashinfer JIT builds break if a conda cross-toolchain leaks in from the parent shell.
