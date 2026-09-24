# VLA Pipeline

End-to-end documentation for building, operating, and deploying the **xArm + Meta Quest** robot system — from hardware assembly through teleoperated data collection, policy training, and on-robot inference.

## What this system does

A human operator wears a **Meta Quest** headset and drives a **UFACTORY xArm** in real time (VR teleoperation), while wrist- and scene-mounted cameras stream back to the headset. Demonstrations are recorded as **LeRobot** datasets, used to train a **vision-language-action (VLA) policy**, which can then drive the arm autonomously.

```
 Operator (Quest)  ── teleop ──▶  xArm + gripper  ── cameras ──▶  LeRobot dataset
                                                                       │
                                                                  train VLA policy
                                                                       │
                                          policy  ── inference ──▶  xArm (autonomous)
```

## Sections

- **[Hardware](hardware/index.md)** — components, bill of materials with purchase links, assembly and networking.
- **[Teleoperation](teleop/index.md)** — setup, day-to-day operation, and dataset recording/processing.
- **[Training](training/index.md)** — policy training pipeline *(coming soon)*.
- **[Inference](inference/index.md)** — loading a trained policy and running it on the robot.

!!! note "Placeholders used throughout"
    Commands, configs and diagrams use placeholders for site-specific values — `<ARM_A_IP>` / `<ARM_B_IP>`, `<WORKSTATION_IP>`, `<IMG_SERVER_IP>`, `<QUEST_A_SERIAL>` / `<QUEST_B_SERIAL>`, camera serials such as `<WRIST_CAM_A_SERIAL>`, and `<HF_USER>`. Replace them with your own. Keep the real values in a private note, **not** in this doc.
