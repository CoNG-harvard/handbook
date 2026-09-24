# Datasets

Recorded sessions land under `~/lerobot/xr_teleoperate/datasets/test_<timestamp>/`. Before training you typically **convert**, optionally **inspect**, and **merge** them.

## Convert for training

Convert a recorded dataset into the processed (`droid_finetune`) format used for training. Output is written to `<dataset-path>_processed` by default.

```bash
python scripts/convert_data_for_finetune.py \
    --dataset-path ~/lerobot/xr_teleoperate/datasets/test_<timestamp>
```

Options:

| Option | Default | Meaning |
|---|---|---|
| `--output-path PATH` | `<dataset-path>_processed` | Output directory |
| `--lpf-cutoff 5.0` | `5.0` | Low-pass filter cutoff (Hz) for state trajectories; `<=0` disables |
| `--lpf-order 2` | `2` | Butterworth filter order |
| `--action-pad 1` | `1` | Zero-pad dims inserted between yaw and gripper in the action |

## Inspect a trajectory

Plot the end-effector XYZ deltas of a recording to sanity-check motion smoothness:

```bash
python scripts/plot_xyz_delta.py ~/lerobot/xr_teleoperate/datasets/test_<timestamp> --target-fps 15
```

## Merge datasets

Combine several **processed** datasets into one training set:

```bash
python scripts/merge_v3_datasets.py \
    --inputs \
        ~/lerobot/xr_teleoperate/datasets/test_<ts1>_processed \
        ~/lerobot/xr_teleoperate/datasets/test_<ts2>_processed \
        ... \
    --output datasets/pick_n_drop_200
```

!!! tip
    Convert each session right after recording, keep a consistent `--dataset.single_task` label per task, then merge the `_processed` directories into one named set (e.g. `pick_n_drop_200`) for training.
