# D1 arm readiness

**Status: arm setup instructions pending.** The Unitree D1 arm is part of the Self Improvement Learning platform. Completing the Go2 navigation guide does not make the arm ready to use. This page records what the project owner must supply before a beginner can set it up.

## Get these from the project owner

- [ ] **Physical installation:** the approved D1 mounting kit, power/data wiring, payload arrangement, and manufacturer instructions for the supplied Go2 and arm.
- [ ] **Robot software:** the exact robot image, SDK versions, companion source revision, network interface, and reviewed local changes.
- [ ] **Arm settings:** confirmed joint limits, gripper behavior, resting pose, and stop/recovery procedure for this physical unit.
- [ ] **Camera and calibration:** the manipulation camera model, serial, mount, and the matching camera-to-arm calibration file, with its storage and restore instructions.
- [ ] **Required services:** the selected manipulation workflow's perception services, model assets, and startup order.
- [ ] **Acceptance record:** a supervised connection, camera, gripper, and bounded movement test, signed off by the operator before a pick/place trial.

Calibration describes where the camera is relative to the arm. A file from another camera mounting arrangement is not interchangeable. Keep a maintained copy of the approved calibration; a temporary `/tmp` file alone is not a durable installation handoff.

## When to continue

The project owner must turn that handoff into a tested installation procedure before this page can provide motion commands. The inspected companion README describes a newer Python environment than the bridge's deployed `walk` environment; that difference also needs resolution for the robot image.

You can continue the [workstation mock check](setup.md) now. The [Go2 camera and navigation path](robot-bridge.md) requires its own commissioned robot and operator checks. See the [source verification record](../getting-started/sources.md#follow-up-source-check) for what was inspected.

??? info "For maintainers: verified source files"
    The inspected companion `LLM_guided_RL` workspace contains the D1 interface (`robot/d1_arm_interface.py`), message definitions, and kinematics. It uses the Unitree SDK to communicate with the arm. The interface can fall back to simulated hardware when the SDK is missing, so importing it successfully is not proof of a working arm connection.

    The active `unidog_nav` workspace also contains manipulation code, including `robot/arm_reach.py` and `robot/skill_pick_pipeline_v2.py`. The reach program expects the companion robot deployment and a camera-to-arm calibration file; its default file location is `/tmp/wrist_handeye.json`. These files are evidence of an existing lab workflow, not a complete fresh-install package.
