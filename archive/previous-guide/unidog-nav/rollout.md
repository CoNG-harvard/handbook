# Legacy closed-loop rollout

!!! note "Advanced reference"
    For an installed system. Historical results below describe earlier lab experiments, not validation of the new setup. Start with the [project guide](index.md) if you are installing for the first time.

Before starting any model service or GPU evaluation here, select the RTX PRO 6000 using [computer preparation](../getting-started/computer.md#select-the-rtx-pro-6000-for-model-programs). NaVILA examples additionally require the [Blackwell-compatible environment](models.md#navila-installation-and-saved-image-check).

This loop remains for historical reproduction. The current V1
planner-specific parser, safe-bin quantization, continuous capture and exact
robot payload flow are documented in [`planner_benchmark/README.md`](https://github.com/CoNG-harvard/unidog_nav/blob/main/planner_benchmark/README.md#live-planner-to-robot-data-flow).

## How the loop works

`scripts/rollout.py` waits for each movement to finish before requesting the next prediction:

1. Capture a fresh camera frame.
2. Build the eight-frame model input from history and the current view.
3. Predict one discrete action and parse it into a robot skill plan.
4. Execute the plan, then capture the next view.
5. End on a stop prediction, failure, or the step limit.

The first motion plan can include standing and readiness checks. A plan may contain several skill calls; the model does not see a new image between calls within that plan.

??? info "Historical example: 12 July 2026"
    Instruction: “Move forward, when seeing the orange chair, turn right and stop.” This trace describes one earlier experiment, not a recommended first test.

    | Cycle | Model output | Execution |
    |---|---|---|
    | 0 | Turn left 45° | Stand, readiness check, left turn |
    | 1 | Turn left 45° | Left turn |
    | 2 | Move forward 75 cm | Forward 0.75 m |
    | 3–6 | Right turns of 45/45/15/45° | Right turns totaling 150° |
    | 7 | Stop | Episode ends |

## Running a real-robot rollout

First complete the current [supervised bring-up](first-run.md), including the real-mode health check. The current all-services preparation script starts Qwen and uses a per-call executor; the old batch-backend expectation from July is not the current startup contract.

Before a NaVILA run, coordinate stopping Qwen so the GPU is available. Then, on the workstation:

```bash
cd "<NAV_DIR>"
conda activate navila
python scripts/rollout.py --planner navila --max-steps 10 \
    --tag my-test --instruction "Turn right and walk to the orange chair. Stop in front of it."
```

This can move the robot repeatedly. Use only as a supervised experiment after single-command tests succeed. For Qwen experiments, use the appropriate Qwen model server and avoid loading NaVILA alongside it.

## V1 structured Qwen live skill-interface test

The older `scripts/rollout.py --planner qwen` path above keeps the legacy
25/50/75 cm free-text action vocabulary. To test the V1 JSON interface,
semantic `speed_level`, safe-bin quantization, F3 image history, executed
action history, operator gate, and robot execution together, use:

```bash
cd "<NAV_DIR>"
conda run -n navila python -m planner_benchmark.run_live \
  --scenario L1-QWEN-V1-NORMAL-1M \
  --planner qwen \
  --repeats 1 \
  --acting-policy F3 \
  --operator "<OPERATOR_NAME>"
```

Run `L1-QWEN-V1-FAST-1M` only after the normal-speed trial passes in a
measured clear lane. Legacy scenarios retain their fixed-increment
`normalization:` for historical comparability and must be run with the explicit
`--normalize` compatibility flag. V1 scenarios use `quantization:`
and log the untouched proposal, executable action, and every transform record.

`--continue-on-failure` is an advanced experiment option that replans after a failed skill. Leave it off for commissioning so a failure ends the attempt. Ctrl+C and `python3 scripts/robot_client.py stop` request a software abort; use the physical stop procedure for unexpected motion.

## Where the results are

One folder per episode: `logs/rollouts/<planner>_<tag>_t<timestamp>/` (tag defaults to the slugified instruction; set `--tag` for a readable name).

- `step_NNN.jpg` — the exact frame the planner saw at cycle N. **#frames = #planning steps.**
- `episode.json` — per step: raw model output, parsed plan, full per-skill `SkillResult`s (measured progress, safety status), `planner_sec`/`robot_sec`, and the batch runner's `timing.setup_s`. Episode `status`: `stopped_by_planner` (planner said stop), `max_steps_reached`, `skill_failed`, `parse_error`, `robot_error`, `interrupted`.

## Writing instructions

NaVILA chooses actions from the instruction and current image; it is not a literal angle-command interpreter. Use explicit directions such as “Turn right and walk to the orange chair. Stop in front of it.” See [offline evaluation](vla-eval.md#phrasing-instructions) for the observed limitations.

The legacy rollout uses a free-text action parser. The live benchmark uses the V1 structured Qwen interface by default; use `--normalize` only to reproduce the older benchmark behavior.

*Historical checks: mock loop, 11 July 2026; supervised NaVILA robot experiment, 12 July 2026. These do not establish RTX PRO 6000 compatibility or performance.*
