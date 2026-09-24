# Offline model evaluation

!!! note "Advanced reference"
    For an installed system. Historical results below describe earlier lab experiments, not validation of the new setup. Start with the [project guide](index.md) if you are installing for the first time.

Use a [Blackwell-compatible NaVILA environment](setup.md#navila-installation-and-saved-image-check) and select the RTX PRO 6000 before running these examples.

`scripts/batch_navila_eval.py` evaluates saved scene/instruction pairs without moving the robot. It loads the model once, prints predictions, and saves JSON results in `logs/`. Run on the workstation in `~/unidog_nav`; obtain the example image folders from the lab.

```bash
cd ~/unidog_nav
conda activate navila

# Single scene, single instruction — the standard single-shot test
python scripts/batch_navila_eval.py \
    --images frames/real_conjested_room1 \
    --query "Move toward the orange chair and stop at a safe distance." \
    --history episode-start

# All scenes under frames/ with one instruction (parent dir auto-expands)
python scripts/batch_navila_eval.py --images frames --history episode-start \
    --query "Turn right toward the open space."

# Cross product: several scenes x several instructions, model loaded once
python scripts/batch_navila_eval.py --history episode-start \
    --images frames/real_conjested_room1 --images frames/real_front_wall1 \
    --query "Turn left." --query "Turn around."

# Fully custom pairs from JSON: [{"scene": ..., "instruction": ...}, ...]
python scripts/batch_navila_eval.py --cases my_cases.json --history episode-start
```

`--images` accepts paths or bare folder names under `frames/`. Without conda activated, wrap any of the above with `scripts/eval_vla.sh` (same arguments).

There is also `scripts/run_navila_test.sh <frames_dir> "<instruction>"`, a thin wrapper around the upstream `llava/eval/run_navigation.py` for a single one-off prediction.

## Checking what the model sees

`scripts/vqa_probe.py` asks the model plain perception questions (no navigation prompt) — use it to rule out image quality before blaming a bad action:

```bash
python scripts/vqa_probe.py frames/real_conjested_room1/0007.jpg \
    "Is there an orange chair in this image? Left, center, or right?"
```

The July 9 lab tests found that NaVILA could locate the orange chair in the supplied images, including mirrored views. This was a scene-specific result; inspect your own camera images and predictions.

## Choose the image history

NaVILA takes eight images: seven history frames and the current view.

| Option | Use it for |
|---|---|
| `--history episode-start` | A single saved view; pads the history with seven black frames, matching the start of an episode |
| `--history asis` (default) | A sequence containing actual robot movement |

In the July 9 tests, eight nearly identical stationary frames biased the model toward “move forward.” Using `episode-start` restored the expected left/right predictions in those tests. If predictions repeat, check the history before changing the checkpoint.

## Phrasing instructions

Use explicit directions, for example: “Turn right and walk toward the orange chair.” The earlier scene tests found that naming an off-center object alone did not reliably produce a turn.

- State the direction if you expect a turn on the first step.
- Avoid relying on qualifiers such as “rightmost” or “at a safe distance.”
- Assess object-goal navigation across a supervised rollout, not a single prediction.

## Interpreting outputs

The model emits text like `The next action is turn right 45 degree.`, parsed into `{action, value, unit}` in the log JSON. The action space is discrete — turn 15/30/45 degrees, move forward 25/50/75 cm, or stop — so e.g. "Turn around." yields a single 45-degree step, not 180: full maneuvers emerge over multiple steps in closed loop. Measure latency on the selected RTX PRO 6000 after validating the Blackwell-compatible environment; earlier timing measurements do not establish performance on this setup.

## VLA text → robot skill plans

`navigation_policy/navila_parser.py` converts raw NaVILA output into the
validated plan format from [`vla_locomotion_skill_interface.md` §2](https://github.com/CoNG-harvard/unidog_nav/blob/main/vla_locomotion_skill_interface.md#2-preferred-skill-combination-format). The old
`scripts/navila_to_skills.py` path remains a thin compatibility CLI.

```bash
python scripts/navila_to_skills.py "The next action is turn right 45 degree."   # one plan
python scripts/navila_to_skills.py --log "<EVALUATION_LOG_JSON>"                 # convert a whole eval log
python scripts/test_navila_to_skills.py                                        # test suite (no pytest needed)
```

Library use: `from navigation_policy.navila_parser import parse_to_plan, VLAParseError`. Legacy scripts may continue importing the compatibility wrapper.
