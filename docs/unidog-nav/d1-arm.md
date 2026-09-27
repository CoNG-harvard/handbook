---
title: Mount and check the D1 arm
---

# Mount and check the D1 arm

The D1 uses Unitree's supported Go2 mounting. Follow the [official payload installation guide](https://support.unitree.com/home/en/developer/Payload), section **Installing the Small Servo Arm**, then complete the camera and operator checks below.

## 1. Mount and connect the arm

1. **Check the kit:** identify the arm, gripper, square rail nuts, M4 × 10 hex-socket screws, and power and Ethernet cables against Unitree's guide.
2. **Mount:** slide the square nuts into the expansion dock rail and secure the arm with the M4 × 10 screws in the orientation the guide shows.
3. **Connect:** run the supplied power and Ethernet cables from the dock to the arm, following Unitree's connection diagram and the port labels on the delivered equipment.
4. **Inspect:** confirm the cables stay clear of the legs, arm joints, and wrist camera, and that the arm's resting position leaves the required clearance inside the gantry.

If the arm is already installed, check its mounting and cable routing without removing it.

## 2. Fit the wrist camera

The wrist camera is a **[RealSense D435](https://www.realsenseai.com/products/stereo-depth-camera-d435/)** (not the front D435i). Clamp it beside the gripper with the [RichBird C-clamp mount](https://www.amazon.com/dp/B0GSR6883N), tighten the clamp and ball head, and leave clearance for the gripper and its cable.

Calibration measures the camera's position relative to the arm, so moving the camera or clamp invalidates it. Record the camera's serial, position, and the calibration target the owner specifies, and keep the calibration record and date with the setup notes.

## 3. Arrange the arm's acceptance check

An experienced operator verifies the gripper, joint limits, resting pose, and stop and recovery procedure before any pick-and-place session, and demonstrates which stop affects the arm and how the arm is supported if power is removed.

**Ready when:** the installer has approved the installation, the calibration matches the installed camera, and the operator's check is recorded.

**Next:** [Hardware readiness](readiness.md)
