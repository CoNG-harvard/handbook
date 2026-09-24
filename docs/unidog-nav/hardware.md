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

| Item and quantity | Why you need it | Selection notes |
|---|---|---|
| **1 Unitree Go2 research robot** | The mobile robot | The companion lab source describes **Go2 Edu Plus**. Confirm the exact edition, control SDK access, and supplied accessories with the owner/vendor; [Unitree Go2 reference](https://www.unitree.com/go2/) |
| **1 Unitree D1 arm with gripper**, robot mounting kit, and matching power/data cables | Adds manipulation to the Go2 | Part of the Self Improvement Learning platform shown above; confirm the complete kit, D1 software interface, and calibration with the lab owner |
| **1 compatible onboard computer** | Runs the bridge and hardware-control software | The source identifies a **Jetson**, but its exact module/RAM/carrier-board model was not verified. It may already be included in the robot package |
| **1 compatible robot battery + charger** | Powers the robot | Confirm inclusion, connector, and charging instructions for the supplied robot. A spare battery is optional |
| **1 manufacturer-supported operator controller/stop interface** | Lets the trained operator control and stop the robot | Confirm the actual supplied controller and demonstrated stop procedure; an SSH terminal is not a physical stop device |
| **1 RealSense D435i camera**, matching USB data cable, and robot mount | Supplies the camera image to the workstation | The supplied platform photo labels this camera as D435i, matching the bridge helper. Confirm its connection and serial during setup; [RealSense camera reference](https://www.realsenseai.com/compare-all-cameras/) |
| **A network connection** between workstation and robot computer | Carries SSH, images, and commands | Provide Ethernet cables and/or the approved wireless network equipment for the chosen deployment |
| **Approved power and mounting for onboard accessories** | Keeps the computer/camera securely powered on the robot | Confirm robot-compatible power connectors, mounts, cable strain relief, and payload arrangement |
| **Clear test area and floor markings** | Makes a supervised short movement test observable | Leave room for the robot to stand and turn; secure loose cables |

The Go2's built-in front camera is an **alternative image source** selected with `--camera front`. It is not automatically selected when a USB camera is absent. Use the same view expected by the model/workflow.

The robot's existing sensing and control interfaces, including the perception inputs used by its motion checks, must work in the commissioned deployment. This list does not call for buying a separate LiDAR without first checking the robot package and software requirements.

## 2. Task-specific accessories {#2-optional-hardware}

The Go2 and D1 arm are both included in the main list above. Add the accessories below for the intended manipulation, voice, or recording workflow.

| Addition | Quantity | Used for |
|---|---|---|
| Arm/wrist camera and calibration target | As specified by the manipulation configuration | Locating and grasping objects; exact camera and bracket specifications require the manipulation handoff |
| DJI Mic Mini transmitter and receiver with USB connection | 1 set | The companion voice guide describes this microphone; its receiver appears as a USB audio device |
| Working audio output | 1 route through the robot or an approved speaker | Spoken feedback; verify the actual output device in the voice setup |
| Spare robot battery and approved storage/charging accessories | According to session length | Longer sessions without waiting for charging |
| Additional logging/backup storage | According to recording volume | Keeping camera frames and experiment logs |

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
