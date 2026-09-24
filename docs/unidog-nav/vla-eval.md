# Running the VLA eval

Main tool: `scripts/batch_navila_eval.py`. It loads the model once, then evaluates every (scene, instruction) pair, prints each prediction, and saves a JSON to `logs/`.

```bash
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

Verified 2026-07-09: on the lab scenes the model correctly finds the orange chair and reports which side it is on (tracks a horizontal mirror flip too), so wide-angle 1920x1080 Go2 frames are perceptually fine. Expect occasional label slips (e.g. a caster chair up close called a "wheelchair").

## The `--history` flag — read this before trusting results

NaVILA takes 8 images: 7 "history" frames + the current observation. What you put in the history changes everything:

- **`--history episode-start` (use this for single-shot tests)** — 7 black frames + the last captured frame as current observation. This exactly matches the official VLN-CE evaluator at t=0 (`sample_and_pad_images` in `repos/NaVILA/evaluation/vlnce_baselines/navila_trainer.py`), i.e. the in-distribution "start of episode" condition.
- **`--history asis` (default)** — feeds all captured frames as history. Only meaningful if the frames actually contain motion (robot moving between frames).

**Known failure mode (confirmed 2026-07-09):** feeding 8 near-identical frames from a standing-still robot is out-of-distribution and collapses the model to "move forward" for *every* instruction — even "Turn left." With `episode-start` on the same scenes, the model followed all turn instructions correctly (10/10 left/right) and chose actions scene-dependently for object-goal instructions (forward when the target was ahead, turn when facing a wall). If every prediction comes back "move forward", check the history before blaming the checkpoint.

## Phrasing instructions

NaVILA was trained on R2R/RxR-style instructions, where turn directions are stated explicitly ("Turn right and walk past the desk..."). Confirmed with a mirror-image test (2026-07-09): at episode start the model does **not** turn toward an off-axis object from its position alone — "Walk to the orange chair" yields "move forward" whether the chair is on the left or the right. Explicit directions work reliably: "The orange chair is on your right. Turn right and walk to it." → turn right 45 degree. Practical rules:

- State the turn direction in the instruction if you expect a turn at step 0.
- Fine-grained referring expressions ("rightmost", "at a safe distance") are out-of-distribution; keep instructions in plain R2R style.
- "Move forward" toward a target that is 20-30 degrees off-axis is not an error — in a closed-loop rollout the agent corrects heading on later steps. Judge object-goal behavior by rollouts, not single predictions.

## Interpreting outputs

The model emits text like `The next action is turn right 45 degree.`, parsed into `{action, value, unit}` in the log JSON. The action space is discrete — turn 15/30/45 degrees, move forward 25/50/75 cm, or stop — so e.g. "Turn around." yields a single 45-degree step, not 180: full maneuvers emerge over multiple steps in closed loop. Expect ~0.5 s per action on the 4090 after a one-time model load.

## VLA text → robot skill plans

`navigation_policy/navila_parser.py` converts raw NaVILA output into the
validated plan format from [`vla_locomotion_skill_interface.md` §2](https://github.com/CoNG-harvard/unidog_nav/blob/main/vla_locomotion_skill_interface.md#2-preferred-skill-combination-format). The old
`scripts/navila_to_skills.py` path remains a thin compatibility CLI.

```bash
python scripts/navila_to_skills.py "The next action is turn right 45 degree."   # one plan
python scripts/navila_to_skills.py --log logs/navila_<...>.json                 # convert a whole eval log
python scripts/test_navila_to_skills.py                                        # test suite (no pytest needed)
```

Library use: `from navigation_policy.navila_parser import parse_to_plan, VLAParseError`. Legacy scripts may continue importing the compatibility wrapper.
