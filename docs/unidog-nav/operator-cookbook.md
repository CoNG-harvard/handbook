# Operator cookbook: voice, YAML scenarios, and direct commands

`~/unidog_nav` owns planners, YAML benchmarks, and the workstation client.
`~/LLM_guided_RL` owns robot-side voice input and safety-gated skills. A
separate development clone also exists; run hardware
commands from the copy actually deployed on the robot.

Commands marked **REAL ROBOT MOVES** require a supervising operator with
e-stop access and a clear workspace.

## 1. Human voice input ("Hey UniDog, ...")

Two selectable command backends on the robot listener
(`--command-backend {hermes,qwen}`, deployed on the dog):

- **qwen** (the voice → Qwen pipeline, live-tested 2026-07-22): the
  transcript goes to the workstation, Qwen plans grounded skill calls, the
  primitive server executes them. This is the default in
  `start_voice_listener.sh`.
- **hermes** (legacy default of the raw listener): the transcript goes to
  the local Hermes agent session. `--real` then requires an explicitly
  narrow `--hermes-toolsets`/`--hermes-skills` set.

```
robot   wake word ("Hey UniDog") -> ASR -> transcript
          |                                              [LLM_guided_RL]
          v  gateway_voice_client.py --------- reverse SSH tunnel :8765
workstation  voice_command_gateway.py                    [unidog_nav]
          |    current camera frame + transcript -> Qwen (vLLM :8000)
          |    -> ordered plan of 1..4 V1 calls (strict JSON array)
          |    -> gate: sanity -> safe-bin quantization -> per-call params
          v  RobotClient ---------------------- SSH tunnel :8766
robot   primitive_server.py --real: stand+ready prologue, guarded primitives,
          sequential execution, abort on first failure
```

### Bring-up (one command per side)

```bash
# Workstation — starts vLLM + tunnels + dog primitive server (over SSH) +
# gateway, idempotently; the gateway is always restarted to pick up code.
bash scripts/start_voice_pipeline.sh up --real   # REAL ROBOT MOVES
bash scripts/start_voice_pipeline.sh up          # no-motion rehearsal
bash scripts/start_voice_pipeline.sh status      # health of all four pieces
bash scripts/start_voice_pipeline.sh down        # stop all but vLLM (--vllm too)
bash scripts/start_voice_pipeline.sh deploy      # push robot-side files

# Robot — inside the vtt env:
cd ~/LLM_guided_RL && bash scripts/start_voice_listener.sh   # REAL ROBOT MOVES
cd ~/LLM_guided_RL && bash scripts/start_voice_listener.sh --dry-run
```

### What you can say

One utterance = one ordered plan of up to 4 V1 skill calls (`move_forward`,
`turn_relative`, `stop`), executed sequentially, open-loop (no re-observation
between calls):

- "move forward one meter"
- "turn right forty-five degrees and move forward half a meter"
- "Hey UniDog, stop" — local e-stop, always works, also preempts a running
  plan mid-motion (client SIGTERM -> gateway `/stop` -> primitive server abort).

Every call is individually validated and quantized to the executable bins
(distances {0.25,0.5,0.75,1.0} m, turns {15,30,45} deg — reduced downward,
never up); any invalid call rejects the whole plan. If a call fails on the
robot (e.g. a clearance sensor timeout), the remaining calls are skipped and
the spoken reply says what did not complete. The robot console prints the
raw Qwen output and the executed calls; the robot speaks the summary
(suffixed "Simulation only..." whenever the primitive server is not in --real).
Speak one utterance at a time and wait for the reply: a command arriving
while one is executing is rejected (busy policy), and stop is the only
exception.

### Contracts and caveats

- The multi-action contract is **gateway-only** (`--single-command`
  reverts): the YAML benchmark path keeps its one-call-per-cycle prompt,
  parser, schema, and gate byte-identical.
- Each command plans from a fresh action history and a fresh camera frame;
  the episode prologue (stand + check_robot_ready) runs before the first
  motion of every command.
- Motion requires BOTH `--real` flags (dog primitive server and listener); in
  listener dry-run/mock the gateway still plans + gates but never executes.
- Never run the voice loop at the same time as another control loop
  (`rollout.py`, `run_vlm_policy.py`, `run_live`).
- Known gaps: backward motion has no primitive ("walk backwards" plans forward
  motion — don't use it); goal-directed utterances ("go to the orange
  chair and stop in front of it") need the future closed-loop episode mode,
  not this single-plan pipeline.

### Debugging

Per-command traces (transcript, raw model output, gated plan, per-skill
robot results, timing) plus the exact camera frame each plan saw land in
`logs/voice_gateway/commands_<date>.jsonl` and `logs/voice_gateway/frames/`;
gateway stdout is `logs/voice_gateway/gateway.log`; the robot-side executor
log is `~/unidog_nav_tools/primitive_server.log` on the dog. Workstation-only
smoke tests (no GPU, no robot):

```bash
python3 robot/primitive_server.py --mock --mock-frames test_frames/real_front_wall1 &
conda run -n navila python scripts/voice_command_gateway.py \
  --planner dummy --robot-url http://127.0.0.1:8766 --once "walk forward"
conda run -n navila python scripts/test_voice_command_gateway.py
```

## 2. Run a YAML benchmark scenario

```bash
# Workstation terminal 1: start Qwen.
cd ~/unidog_nav
bash agent_ai/start_vllm.sh

# Terminal 2: preflight, then run one YAML. REAL ROBOT MAY MOVE.
cd ~/unidog_nav
bash scripts/prepare_real_robot.sh --check
conda run -n navila python -m planner_benchmark.run_live \
  --scenario planner_benchmark/scenarios/L1-QWEN-V1-NORMAL-1M.yaml \
  --planner qwen --repeats 1 --acting-policy F3 --operator <name>

# The scenario-name form is equivalent.
conda run -n navila python -m planner_benchmark.run_live \
  --scenario L1-QWEN-V1-NORMAL-1M \
  --planner qwen --repeats 1 --acting-policy F3 --operator <name>

# Or run a suite from scenarios/suites.yaml.
conda run -n navila python -m planner_benchmark.run_suite \
  --suite v1_qwen_skill_interface \
  --planner qwen --repeats 1 --acting-policy F3 --operator <name>
```

Do not add `--yes`, `--no-confirmation`, or `--no-annotation` to real
collection. Run the FAST case only after NORMAL passes in a measured clear
lane. See [the benchmark runbook](https://github.com/CoNG-harvard/unidog_nav/blob/main/planner_benchmark/README.md) for mock tests.

## 3. Send a command directly to the robot

```bash
# Preferred workstation path through the bridge.
cd ~/unidog_nav
ssh -f -N -L 8766:127.0.0.1:8766 unitree
python3 scripts/robot_client.py health       # verify "real": true
python3 scripts/robot_client.py start-episode

# REAL ROBOT MOVES.
python3 scripts/robot_client.py exec "The next action is turn left 15 degrees."
python3 scripts/robot_client.py exec "The next action is move forward 25 cm."
python3 scripts/robot_client.py stop         # stop/abort from another terminal
```

For on-robot diagnostics, call the sanctioned skill entry point:

```bash
cd ~/LLM_guided_RL
conda run -n walk python scripts/run_skill.py --list
conda run -n walk python scripts/run_skill.py move_forward \
  --params '{"distance_m": 0.25}'             # dry-run

# REAL ROBOT MOVES; omit --yes to keep interactive confirmation.
conda run -n walk python scripts/run_skill.py move_forward \
  --params '{"distance_m": 0.25}' --real --ip eth0
conda run -n walk python scripts/run_skill.py turn_relative \
  --params '{"dyaw_deg": 15}' --real --ip eth0
```

Prefer these paths over raw SDK snippets: they preserve validation, readiness
preparation, LiDAR guarding, cleanup, and stop handling.
