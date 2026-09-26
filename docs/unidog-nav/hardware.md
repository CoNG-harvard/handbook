# Self Improvement Learning hardware

**Goal:** assemble the Self Improvement Learning platform: **one Unitree Go2 robot with one Unitree D1 arm**, its cameras, onboard computer, and control equipment. Check the dog and the mounted arm separately before a combined session.

The [workstation with RTX PRO 6000, display/input devices, storage, and shared network equipment](../getting-started/hardware.md#shared-equipment-prepare-once) also serve VLA Pipeline. Count them once in the shared setup; the list below contains **equipment specific to Self Improvement Learning**.

<figure class="handbook-figure" markdown="1">

![Self Improvement Learning platform photograph labeled with the Unitree Go2, Unitree D1 arm, and D435i camera.](assets/platform.png)

<figcaption markdown="1">

Self Improvement Learning platform with a D1 arm and D435i camera. The arm requires its own mounting and calibration checks.

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

- **Robot:** the lab reference specifies [Go2 Edu Plus](https://www.unitree.com/go2/). Confirm the exact edition, supported control interface, and included accessories with the owner/vendor.
- **D1 arm:** include its complete mounting and cable kit. **Arm commissioning is pending**; obtain the [D1 mounting and calibration plan](d1-arm.md) before manipulation.
- **Onboard computer:** the lab reference identifies a Jetson, but its exact module, memory, and carrier board were not verified. Check whether it is included with the robot.
- **Battery and controller:** confirm the approved charger, connectors, and demonstrated stop procedure. Keep the operator's stop interface accessible.
- **Camera:** the supplied photo identifies a [D435i](https://www.realsenseai.com/compare-all-cameras/), used on this platform. Record its serial and verify its USB connection on the robot.
- **Connections and mounts:** use the approved Ethernet or wireless connection. Confirm accessory power, payload arrangement, cable strain relief, and space to stand and turn.

The Go2 also has a built-in front camera. It is a different device and view from the added D435i; confirm which camera the planned session uses. Check the robot package before purchasing additional sensing equipment.

## 2. Task-specific accessories {#2-optional-hardware}

The Go2 and D1 arm are both included in the main list above. Add the accessories below for the intended manipulation, voice, or recording workflow.

| Additional equipment | Quantity |
|---|---|
| Manipulation camera and calibration target | Specified by owner |
| DJI Mic Mini transmitter/receiver with USB connection | 1 set for voice |
| Robot audio output or approved speaker | 1 route for voice |
| Spare battery and approved charging/storage accessories | As needed |
| Extra logging and backup storage | As needed |

The manipulation handoff must specify the camera, bracket, and calibration target. For a voice-equipped station, verify the USB microphone connection and audio output during setup. Size spare batteries and storage for the session length and recording volume.

Microphones and speakers are task-specific accessories; a Quest headset is not part of this platform's core equipment. Complete the D1 mounting, calibration, and supervised checks before using the arm.

## 3. Understand the connections

```text
Shared workstation ── network link ── robot's onboard computer
                                      │
                         ┌────────────┼─────────────┐
                         │            │             │
                    Go2 control   USB camera   optional USB mic
```

The shared workstation stays off the robot and also serves the arm project. Have the installer confirm the onboard computer's connections to the robot and accessories using the supplied wiring instructions. Connect the D1 through its approved power/data arrangement; the diagram shows the main network and camera connections only.

For an initial network check, use the approved connection method. Before a walking test, remove or manage any tether according to the operator's procedure so the robot cannot pull a workstation cable or trip over it.

## 4. Check the delivered package

- [ ] Robot edition and control interface match the intended platform.
- [ ] Onboard computer model, architecture, storage, power, and connections are documented.
- [ ] Battery, charger, controller, and stop procedure are available.
- [ ] Camera model, USB cable, mount, and selected image source agree.
- [ ] Access to the shared workstation and its network connection is arranged.
- [ ] Network connections and accessory mounts are ready.
- [ ] D1 arm, gripper, mounting kit, and power/data cables are included; calibration and stop procedures are recorded.
- [ ] Task-specific camera, voice, and storage accessories are listed separately.

**Next:** review [D1 arm readiness](d1-arm.md), then complete the [platform readiness checklist](readiness.md).
