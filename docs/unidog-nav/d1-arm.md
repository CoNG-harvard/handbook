---
title: D1 arm readiness
---

# D1 arm readiness

The D1 uses Unitree's supported Go2 mounting arrangement. Follow the [official Go2 payload installation guide](https://support.unitree.com/home/en/developer/Payload), under **Installing the Small Servo Arm**, then complete the camera and operator checks below.

## 1. Mount and connect the arm

1. **Check the kit:** identify the supplied arm, gripper, rail nuts, screws, and power/data cables against Unitree's guide.
2. **Mount:** position the square nuts in the expansion dock's rail and secure the arm with the M4 × 10 hex-socket screws specified by Unitree. Follow the guide's illustrated orientation.
3. **Connect:** use the supplied power and Ethernet cables between the dock and arm, following Unitree's connection diagram and the delivered equipment's port labels.
4. **Inspect:** check that cables remain clear of the legs, arm joints, and wrist camera, and that the arm's resting position leaves the required clearance.

Use the delivered manufacturer's instructions for power-off handling and fastening requirements. If the arm is already installed, check its mounting and cable routing without removing it. Check the added wrist-camera mount and gantry clearance separately.

## 2. Identify the camera and calibration

The D1 wrist camera beside the gripper is a **[RealSense D435](https://www.realsenseai.com/products/stereo-depth-camera-d435/)**, confirmed by the project owner. It is separate from the front **D435i**. Record its serial, mounting position, and the calibration target specified by the owner. Calibration measures the camera's position relative to the arm. Moving the camera or mount can invalidate those measurements.

Use the [RichBird C-clamp camera mount](https://www.amazon.com/dp/B0GSR6883N) for the D435 wrist camera. Check that the clamp and ball head are secure and leave clearance for the gripper and camera cable before calibration.

Keep the approved calibration record and its date with the private setup notes. The pictured D435i does not establish which camera arrangement is approved for every manipulation task.

## 3. Arrange the arm's acceptance check

An experienced operator must verify the gripper, limits, resting pose, and stop/recovery procedure before a pick-and-place session. Have the operator demonstrate which stop affects the arm and how the arm is supported if power is removed.

**Ready only when:** the installer has approved the physical installation, the calibration matches the installed camera, and the supervised arm check is recorded. Return to [platform readiness](readiness.md) with any outstanding items listed.
