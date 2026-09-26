# Self Improvement Learning hardware

**Goal:** assemble the Self Improvement Learning platform: **one Unitree Go2 robot with one Unitree D1 arm**, its cameras, onboard computer, and control equipment. The initial software checks focus on navigation; arm control is configured separately.

The [workstation with RTX PRO 6000, display/input devices, storage, and shared network equipment](../getting-started/hardware.md#shared-equipment-prepare-once) also serve VLA Pipeline. Count them once in the shared setup; the list below contains **equipment specific to Self Improvement Learning**.

<figure class="handbook-figure" markdown="1">

![Self Improvement Learning platform photograph labeled with the Unitree Go2, Unitree D1 arm, and D435i camera.](assets/platform.png)

<figcaption markdown="1">

Self Improvement Learning platform with a D1 arm and D435i camera. The first navigation steps do not use arm control.

[View full-size image](assets/platform.png) · [Source PDF](assets/platform.pdf)
{ .figure-links }

</figcaption>

</figure>

## 1. Core platform hardware {#1-core-equipment-for-navigation}

| Equipment | Quantity |
|---|---|
| Unitree Go2 research robot | 1 |
| Unitree D1 arm and gripper | 1 set |
| D1 mounting kit and power/data cables | 1 set |
| Compatible onboard computer | 1 |
| Robot battery and charger | 1 set |
| Supported operator controller/stop interface | 1 |
| RealSense D435i, USB data cable, and mount | 1 set |
| Robot network connection | 1 |
| Approved accessory power, mounts, and cable restraints | As needed |
| Clear test area and floor markings | 1 area |

### Selection details

- **Robot:** the companion source describes [Go2 Edu Plus](https://www.unitree.com/go2/). Confirm the exact edition, SDK access, and included accessories with the owner/vendor.
- **D1 arm:** include its complete mounting and cable kit. **Arm commissioning is pending**; obtain the [D1 software and calibration handoff](d1-arm.md) before manipulation.
- **Onboard computer:** the source identifies a Jetson, but its exact module, memory, and carrier board were not verified. Check whether it is included with the robot.
- **Battery and controller:** confirm the approved charger, connectors, and demonstrated stop procedure. A workstation terminal does not replace the operator's stop interface.
- **Camera:** the supplied photo identifies a [D435i](https://www.realsenseai.com/compare-all-cameras/), matching the bridge helper. Record its serial and verify its USB connection on the robot.
- **Connections and mounts:** use the approved Ethernet or wireless deployment. Confirm accessory power, payload arrangement, cable strain relief, and space to stand and turn.

The Go2's built-in front camera is an **alternative image source** selected with `--camera front`. It is not automatically selected when a USB camera is absent. Use the same view expected by the model/workflow.

The robot's existing sensing and control interfaces, including the perception inputs used by its motion checks, must work in the commissioned deployment. This list does not call for buying a separate LiDAR without first checking the robot package and software requirements.

## 2. Task-specific accessories {#2-optional-hardware}

The Go2 and D1 arm are both included in the main list above. Add the accessories below for the intended manipulation, voice, or recording workflow.

| Additional equipment | Quantity |
|---|---|
| Manipulation camera and calibration target | Specified by owner |
| DJI Mic Mini transmitter/receiver with USB connection | 1 set for voice |
| Robot audio output or approved speaker | 1 route for voice |
| Spare battery and approved charging/storage accessories | As needed |
| Extra logging and backup storage | As needed |

The manipulation handoff must specify the camera, bracket, and calibration target. The companion voice guide describes the DJI microphone as a USB audio device; verify both audio input and output during voice setup. Size spare batteries and storage for the session length and recording volume.

Navigation-only setup does not require arm control, a microphone, or a Quest headset. Before using the installed D1 arm, complete its mounting, calibration, software, and supervised checks.

## 3. Understand the connections

```text
Shared workstation ── network / SSH ── robot's onboard computer
                                      │
                         ┌────────────┼─────────────┐
                         │            │             │
                    Go2 control   USB camera   optional USB mic
```

The shared workstation stays off the robot and also serves the arm project. The onboard computer must reach the robot's hardware interfaces as configured by the manufacturer/lab image. A workstation Ethernet cable is not a replacement for that internal setup.

For an initial network check, use the deployment's approved connection method. Before a walking test, remove or manage any tether according to the operator's procedure so the robot cannot pull a workstation cable or trip over it.

## 4. Check the delivered package

- [ ] Robot edition and SDK access match the lab's control software.
- [ ] Onboard computer model, architecture, storage, power, and installed robot image are documented.
- [ ] Battery, charger, controller, and stop procedure are available.
- [ ] Camera model, USB cable, mount, and selected image source agree.
- [ ] Access to the shared workstation is arranged, with the correct Self Improvement Learning environment and GPU available.
- [ ] Network connections and accessory mounts are ready.
- [ ] D1 arm, gripper, mounting kit, and power/data cables are included; calibration and control setup are recorded.
- [ ] Task-specific camera, voice, and storage accessories are listed separately.

**Next:** [Prepare the workstation](../getting-started/computer.md), then [install Self Improvement Learning](setup.md). For the robot-side software handoff, see [bridge preparation](robot-bridge.md#1-prepare-the-robot-computer-with-the-platform-owner).
