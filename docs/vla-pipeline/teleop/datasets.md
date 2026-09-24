# Prepare your recordings

A **dataset** contains saved episodes, camera images, and recorded robot information. Keep the original recording; write converted data into a new folder.

## 1. Locate a saved session

Use the exact dataset path printed by the launcher. The current launcher writes new recordings under `~/lerobot/datasets/`; older sessions may be under `~/lerobot/xr_teleoperate/datasets/`.

```bash
ls "<RECORDED_DATASET>/meta"
```

Replace the placeholder with your session folder. Confirm that at least one episode was saved before converting it.

## 2. Convert it for the intended model

The lab conversion script prepares LeRobot v3 data for its Cartesian-action training workflow. Check with the model owner whether this converter matches the intended checkpoint/training configuration; waypoint and other workflows can use different converters.

```bash
cd ~/lerobot
conda activate lerobot
python scripts/convert_data_for_finetune.py \
  --dataset-path "<RECORDED_DATASET>" \
  --output-path "<NEW_PROCESSED_DATASET>"
```

Use a new output path. The inspected default target rate is 15 frames per second, with action padding and trajectory filtering controlled by the script's options. See them without starting hardware:

```bash
python scripts/convert_data_for_finetune.py --help
```

**Expected:** the command completes and the processed output contains metadata and data files. Confirm task labels, image orientation, episode count, and action units with the model owner.

## 3. Merge compatible processed sessions, if needed

```bash
cd ~/lerobot
conda activate lerobot
python scripts/merge_v3_datasets.py \
  --inputs "<PROCESSED_SESSION_1>" "<PROCESSED_SESSION_2>" \
  --output "<NEW_MERGED_DATASET>"
```

Merge only sessions with compatible camera names, feature layouts, action meanings, and frame rates. Retain the original folders and record which sessions were included.

## 4. Hand off the dataset

Tell the model owner where the data is, which station recorded it, what the task labels mean, and whether anything changed in camera mounting or control settings. Record failures separately from successful demonstrations.

**Next:** [Model handoff](../training/index.md) explains the information needed to use a resulting checkpoint.
