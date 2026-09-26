# D1 arm readiness

**Status: platform-specific assembly and commissioning instructions are pending.** The D1 is part of the Go2 platform, but it needs its own mounting, calibration, and operator checks.

## 1. Confirm the mounting and power plan

Obtain the manufacturer's instructions and the project owner's approved arrangement for the exact Go2 and D1 units. Have the installer confirm:

- The mounting kit, fasteners, base attachment, and gripper are complete.
- The payload and its placement are acceptable for the robot.
- Power supplies, connectors, and data cables match the delivered equipment.
- Cables cannot catch on the arm, legs, or camera mount.
- The arm's resting position leaves the required clearance for the dog.

This handbook does not supply mounting torque, wiring pinouts, or load limits; use the exact manufacturer's instructions for those details.

## 2. Identify the camera and calibration

The D1 wrist camera beside the gripper is a **RealSense D435**, confirmed by the project owner. It is separate from the front **D435i**. Record its serial, mounting position, and the calibration target specified by the owner. Calibration measures the camera's position relative to the arm. Moving the camera or mount can invalidate those measurements.

Keep the approved calibration record and its date with the station record. The pictured D435i does not establish which camera arrangement is approved for every manipulation task.

## 3. Arrange the arm's acceptance check

An experienced operator must verify the gripper, limits, resting pose, and stop/recovery procedure before a pick-and-place session. Have the operator demonstrate which stop affects the arm and how the arm is supported if power is removed.

**Ready only when:** the installer has approved the physical installation, the calibration matches the installed camera, and the supervised arm check is recorded. Return to [platform readiness](readiness.md) with any outstanding items listed.
