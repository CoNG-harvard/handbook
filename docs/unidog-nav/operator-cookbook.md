# Voice and benchmark experiments

!!! note "Advanced reference"
    For an installed system. Complete [bridge setup](robot-bridge.md) and [first supervised movement](first-run.md) before using hardware commands. Earlier lab results do not validate a new installation.

Run workstation commands in `~/unidog_nav`. Robot commands use the deployed `~/LLM_guided_RL` checkout. Select the [RTX PRO 6000](../getting-started/computer.md#select-the-rtx-pro-6000-for-model-programs) and follow the [shared-workstation handover](../getting-started/hardware.md#using-the-shared-workstation) before starting a model. Commands using `navila` need its [Blackwell-compatible environment](setup.md#navila-installation-and-saved-image-check).

## 1. Voice control

The robot listener converts speech into text. The workstation combines that text with a camera image, asks Qwen for a plan, validates the actions, and sends them to the robot bridge.

| Component | Location | Connection |
|---|---|---|
| Voice listener | Robot | Sends the transcript through a reverse SSH tunnel on port 8765 |
| Voice gateway | Workstation | Uses the Qwen server on port 8000 |
| Robot bridge | Robot | Receives commands through the workstation tunnel on port 8766 |

The launcher defaults to the **Qwen** backend. The raw listener also supports the legacy **Hermes** backend; real Hermes execution requires a restricted `--hermes-toolsets`/`--hermes-skills` configuration from the maintainer.

### Start a supervised voice session

!!! warning "Real motion is enabled"
    The following launchers enable robot execution. Keep an operator at the physical stop control. Do not run voice control alongside another robot controller.

**Workstation:**

```bash
cd ~/unidog_nav
bash scripts/start_voice_pipeline.sh up --real
```

This starts the model, tunnels, robot bridge, and gateway; the gateway restarts to load the current code. The robot also needs the voice environment and optional hardware from the [equipment list](hardware.md#2-optional-hardware).

**Robot, inside the lab-provided `vtt` environment:**

```bash
cd ~/LLM_guided_RL
bash scripts/start_voice_listener.sh
```

For a rehearsal, omit `--real` from the workstation launcher and use `--dry-run` on the robot listener. Inspect service status and actual bridge mode; do not assume an existing service has changed mode.

### Give one instruction at a time

Examples include “move forward one meter” and “turn right forty-five degrees and move forward half a meter.” Wait for the spoken reply before the next instruction.

- Each instruction produces up to four calls: `move_forward`, `turn_relative`, or `stop`.
- Calls run in order, without a new camera observation between them.
- Distances are rounded down to supported values: 0.25, 0.5, 0.75, or 1 m. Turns use 15, 30, or 45 degrees.
- An invalid call rejects the plan; a failed call skips the remaining calls.
- The first motion of each instruction can include standing and readiness checks.
- “Hey UniDog, stop” requests a software abort. It depends on the listener and connection; use the physical stop for unexpected motion.

**Known limits:** backward motion has no supported primitive; do not request it. Object-goal instructions such as “go to the chair” require a separate loop that observes again after movement. A new instruction is rejected while a plan is running, except for stop.

### Status, logs, and shutdown

On the workstation:

```bash
cd ~/unidog_nav
bash scripts/start_voice_pipeline.sh status
```

| Output | Location |
|---|---|
| Transcripts, plans, results, and timing | `logs/voice_gateway/commands_<date>.jsonl` |
| Camera frames used for planning | `logs/voice_gateway/frames/` |
| Gateway output | `logs/voice_gateway/gateway.log` |
| Voice launcher's robot executor log | `~/unidog_nav_tools/primitive_server.log` on the robot |

Stop the robot and listener before shutting down the workstation pipeline:

```bash
cd ~/unidog_nav
bash scripts/start_voice_pipeline.sh down
```

This leaves vLLM running. Stop the model separately only when no other user needs it. The `deploy` subcommand copies robot-side files; use it only for a coordinated update.

### Check the gateway without hardware

Start the [mock bridge on port 18766](setup.md#2-run-a-mock-bridge-with-no-robot), then use another workstation terminal:

```bash
cd ~/unidog_nav
conda run -n navila python scripts/voice_command_gateway.py \
  --planner dummy --robot-url http://127.0.0.1:18766 --once "walk forward"
conda run -n navila python scripts/test_voice_command_gateway.py
```

These checks do not load a GPU model or move a robot. Stop the mock bridge afterward.

## 2. Run a benchmark scenario

Start Qwen using [model setup](setup.md#qwen-installation-and-check), and complete the supervised real-mode bridge startup. The preflight below reports status; it does not start the bridge.

!!! warning "This scenario can move the robot"
    Use a measured, clear test area and an operator at the stop control. Run the normal-speed case before any fast case.

In another workstation terminal, replace `<OPERATOR_NAME>` with your name:

```bash
cd ~/unidog_nav
bash scripts/prepare_real_robot.sh --check
conda run -n navila python -m planner_benchmark.run_live \
  --scenario L1-QWEN-V1-NORMAL-1M \
  --planner qwen --repeats 1 --acting-policy F3 --operator "<OPERATOR_NAME>"
```

The scenario may also be specified by its YAML path, such as `planner_benchmark/scenarios/L1-QWEN-V1-NORMAL-1M.yaml`. To run a reviewed suite instead:

```bash
conda run -n navila python -m planner_benchmark.run_suite \
  --suite v1_qwen_skill_interface \
  --planner qwen --repeats 1 --acting-policy F3 --operator "<OPERATOR_NAME>"
```

Keep operator confirmation and annotation enabled: do not add `--yes`, `--no-confirmation`, or `--no-annotation`. The voice gateway's multi-action format does not apply to this benchmark's one-call-per-cycle format. See the [benchmark runbook](https://github.com/CoNG-harvard/unidog_nav/blob/main/planner_benchmark/README.md) for scenario definitions and mock tests.

## 3. Direct robot commands

Use [First supervised movement](first-run.md) for workstation commands through the bridge, including startup and shutdown. For diagnostics **on the robot**, the approved skill entry point provides a list and a dry run:

```bash
cd ~/LLM_guided_RL
conda run -n walk python scripts/run_skill.py --list
conda run -n walk python scripts/run_skill.py move_forward \
  --params '{"distance_m": 0.25}'
```

The following **moves the robot**. Use only with the operator ready, and keep interactive confirmation enabled:

```bash
conda run -n walk python scripts/run_skill.py move_forward \
  --params '{"distance_m": 0.25}' --real --ip eth0
```

`eth0` is the reference interface name; use the owner's configured interface. This entry point retains the lab's validation, readiness checks, motion guards, and stop handling. Follow the [session shutdown procedure](first-run.md#5-end-the-session) when finished.
