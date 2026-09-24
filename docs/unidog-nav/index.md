# UniDog Nav

Workspace for testing vision-language navigation (VLN/VLA) models on a Unitree Go2 robot dog. The current focus is evaluating [NaVILA](https://github.com/AnjieCheng/NaVILA) (navila-llama3-8b-8f) on frames captured from the Go2's front camera, before moving to closed-loop control.

Code: [CoNG-harvard/unidog_nav](https://github.com/CoNG-harvard/unidog_nav), cloned on the workstation at `~/unidog_nav`.

!!! note "Placeholders"
    Site-specific values are written as placeholders, e.g. `<DOG_IP>`. Keep the real values in a private note, **not** in this doc.

## Layout

| Path | What it is |
|---|---|
| `scripts/` | CLI entry points and the robot client; `navila_to_skills.py` is a compatibility wrapper |
| `navigation_policy/` | Shared Qwen/NaVILA policy contracts and canonical NaVILA parser |
| `planner_benchmark/` | Current live runner, safe-bin quantization, frame history and benchmark docs |
| `robot/` | Code deployed to the Go2's onboard PC (`primitive_server.py`) |
| `frames/` | Captured Go2 camera scenes — one folder per capture: 8 JPGs (1920x1080) + `metadata.json` |
| `logs/` | Eval results, one JSON per run: `navila_<scene>_t<timestamp>.json` |
| `models/navila-llama3-8b-8f/` | NaVILA checkpoint (VILA-style: `llm/`, `mm_projector/`, `vision_tower/`) |
| `repos/NaVILA/` | Upstream NaVILA repo (provides `llava/` and the official VLN-CE evaluator) |
| `agent_ai/` | Separate Qwen3-VL-8B vLLM server (OpenAI-compatible API on `:8000`, own `.venv`) — unrelated to NaVILA |

## Environments

- **Real world experiments** run in the conda env `navila`. Either `conda activate navila` first, or use `scripts/eval_vla.sh`, which activates it for you.
- **GPU is exclusive**: the model needs most of the RTX 4090's 24 GB. The Qwen vLLM server (`agent_ai/start_vllm.sh`) fills the card — stop it before running NaVILA, and vice versa.

## Pages in this manual

- **[Quick reference](quick-reference.md)**: everyday commands.
- **[Workstation ↔ robot bridge](robot-bridge.md)**: SSH tunnel, dog-side server, collecting frames.
- **[Operator cookbook](operator-cookbook.md)**: voice pipeline, YAML benchmark scenarios, direct robot commands.
- **[Running the VLA eval](vla-eval.md)**: offline NaVILA evaluation on captured frames, and parsing its output into skill plans.
- **[Legacy closed-loop rollout](rollout.md)**: the original perceive → plan → act loop.
- **[Status and roadmap](roadmap.md)**: findings so far and open design questions.

## More docs in the code repo

These live next to the code and change with it:

- [planner_benchmark/README.md](https://github.com/CoNG-harvard/unidog_nav/blob/main/planner_benchmark/README.md): live runner, safe-bin quantization, benchmark workflow
- [navigation_policy/README.md](https://github.com/CoNG-harvard/unidog_nav/blob/main/navigation_policy/README.md): NaVILA / Qwen-VL behind one interface
- [agentic_planner/README.md](https://github.com/CoNG-harvard/unidog_nav/blob/main/agentic_planner/README.md): task-level planning over the robot's live primitive registry
- [finetune/FINETUNE_README.md](https://github.com/CoNG-harvard/unidog_nav/blob/main/finetune/FINETUNE_README.md): Qwen3-VL-8B training on the RTX Pro 6000 box
- [tasks/README.md](https://github.com/CoNG-harvard/unidog_nav/blob/main/tasks/README.md), [ROUND1_CHECKLIST.md](https://github.com/CoNG-harvard/unidog_nav/blob/main/tasks/ROUND1_CHECKLIST.md), [FLOOR_MARKERS.md](https://github.com/CoNG-harvard/unidog_nav/blob/main/tasks/FLOOR_MARKERS.md): task design, operator checklist, floor layout
- [vla_locomotion_skill_interface.md](https://github.com/CoNG-harvard/unidog_nav/blob/main/vla_locomotion_skill_interface.md): VLA → locomotion skill interface reference
