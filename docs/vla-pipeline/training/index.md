# Training Overview

!!! note "Coming soon"
    This section is a placeholder — the training pipeline will be documented here. The outline below marks what it will cover.

Training takes the **processed** datasets from [Teleoperation → Datasets](../teleop/datasets.md) and produces a policy checkpoint that the [Inference](../inference/index.md) section loads onto the robot.

## Planned contents

- **Data preparation** — which processed datasets to use, the `droid_finetune` format, train/val split.
- **Policy & config** — which policy architecture (e.g. ACT / a VLA backbone), key hyperparameters, observation/action shapes (these depend on the xArm model and camera set).
- **Launching training** — the `lerobot-train` command, where checkpoints are written, expected runtime.
- **Monitoring** — logs/metrics to watch, loss curves, when to stop.
- **Outputs** — the checkpoint directory to hand to inference.

## Inputs / outputs (summary)

```
 datasets/*_processed  ──▶  lerobot-train  ──▶  checkpoint  ──▶  Inference (lerobot-record --policy.path)
```
