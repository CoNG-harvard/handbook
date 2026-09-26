---
title: Self Improvement Learning hardware
---

# Self Improvement Learning hardware

**Goal:** assemble the Self Improvement Learning platform: **one Unitree Go2 Education Plus (EDU Plus) robot with one Unitree D1 arm**, its cameras, onboard computer, and control equipment. Check the dog and the mounted arm separately before a combined session.

The [workstation with RTX PRO 6000, display/input devices, storage, and shared network equipment](../getting-started/hardware.md#shared-equipment-prepare-once) also serve VLA Pipeline and ABC Box. Count them once in the shared setup; the list below contains **equipment specific to Self Improvement Learning**.

[Identify the parts in the labeled photograph](index.md) — the Go2, D1 arm, front D435i, and D435 wrist camera.

## 1. Core platform hardware {#1-core-equipment-for-navigation}

Product links identify known models. **Catalogs** and assembly **references** cover unspecified parts; confirm exact sizes, compatibility, and included accessories before ordering.

| Equipment | Quantity | Product or reference |
|---|---|---|
| Unitree Go2 Education Plus (EDU Plus), including onboard computer | 1 set | [Unitree Go2](https://www.unitree.com/go2/) — edition confirmed by project owner |
| Unitree Go2 Protective Bracket / Gantry for Go2 EDU | 1 | [RobotShop listing](https://www.robotshop.com/products/unitree-go2-protective-bracket-gantry-go2-edu) |
| Unitree D1 arm and gripper | 1 set | [D1 arm — US Robot Store](https://www.usrobotstore.com/products/unitree-go2-servo-robotic-arm-d1) — confirm exact package |
| D1 mounting kit and power/data cables | 1 set | [Unitree mounting and connections](https://support.unitree.com/home/en/developer/Payload) — small servo arm section; check supplied kit |
| Robot battery and charger | 1 set | [Go2 battery](https://shop.unitree.com/products/go2-battery) · [charger](https://shop.unitree.com/products/unitree-go2-charger) — match delivered variant |
| Supported operator controller/stop interface | 1 | [Go2 controller](https://shop.unitree.com/products/go2-controller) — confirm supported stop function |
| RealSense D435i front camera, USB data cable, and mount | 1 set | [D435i](https://www.realsenseai.com/products/depth-camera-d435i/) · [USB cable catalog](https://www.startech.com/en-us/cables/usb-30) — mount to specify |
| RealSense D435 wrist camera and USB data cable | 1 set | [D435](https://www.realsenseai.com/products/stereo-depth-camera-d435/) · [USB cable catalog](https://www.startech.com/en-us/cables/usb-30) |
| RichBird 60 mm C-clamp mount with ball head and 1/4-inch screw for the D1 wrist camera | 1 | [RichBird mount](https://www.amazon.com/dp/B0GSR6883N) |
| Robot network connection | 1 | [Ethernet cable catalog](https://www.startech.com/en-us/cables/network) — confirm wired/wireless arrangement |
| Approved accessory power, mounts, and cable restraints | As needed | [Unitree accessories](https://shop.unitree.com/collections/all) · [cable ties](https://www.mcmaster.com/products/cable-ties/) — verify power and mounts |
| Clear test area and floor markings | 1 area | [Floor-marking tape catalog](https://www.mcmaster.com/products/floor-marking-tape/) — follow the approved test layout |

### Photo count check

The supplied picture shows **1 Go2, 1 D1 arm, and 2 external cameras**: the labeled front **D435i** and a **D435 wrist camera** beside the gripper. The wrist camera model was confirmed by the project owner; both cameras are included in the core list above. The built-in front camera is part of the Go2 and is not an extra purchase. Battery, charger, controller, and cable quantities cannot be verified from this view.

### Selection details

- **Robot:** the project owner confirmed [Go2 Education Plus (EDU Plus)](https://www.unitree.com/go2/). Check the supported control interface and included accessories against the delivered package.
- **Protective gantry:** an external support frame for Go2 EDU posture and movement experiments. RobotShop lists one gantry per package (SKU **RB-Unt-97**, manufacturer part **Go2-Protective-Bracket**). It is not shown in the platform photo. Confirm the attachment arrangement, supported load, and clearance with the mounted D1 arm before use.
- **D1 arm:** follow [Unitree’s official mounting and connection instructions](https://support.unitree.com/home/en/developer/Payload) for the Go2 expansion dock. Check the supplied kit, then complete [D1 arm readiness](d1-arm.md) before manipulation.
- **Onboard computer:** included with this Go2 EDU Plus setup; no separate purchase is needed. Use the supplied computer and its documented connections.
- **Battery and controller:** confirm the approved charger, connectors, and demonstrated stop procedure. Keep the operator's stop interface accessible.
- **Cameras:** use one front [D435i](https://www.realsenseai.com/products/depth-camera-d435i/) and one [D435](https://www.realsenseai.com/products/stereo-depth-camera-d435/) at the D1 wrist. Record each camera's serial, mounting position, and USB connection separately.
- **D1 wrist camera mount:** use the linked RichBird C-clamp mount selected for this platform. The listing specifies a 360° ball head and a 1/4"-20 camera screw. During installation, secure the clamp and ball head, leave cable slack, and check clearance around the gripper and wrist.
- **Connections and mounts:** use the approved Ethernet or wireless connection. Confirm accessory power, payload arrangement, cable strain relief, and space to stand and turn.

The Go2 also has a built-in front camera. It is a different device and view from the added D435i; confirm which camera the planned session uses. Check the robot package before purchasing additional sensing equipment.

## 2. Task-specific accessories {#2-optional-hardware}

The Go2 and D1 arm are both included in the main list above. Add the accessories below for the intended manipulation, voice, or recording workflow.

| Additional equipment | Quantity | Product or reference |
|---|---|---|
| Manipulation calibration target | Specified by owner | [Calibration-target example](https://calib.io/products/kalibr-targets) — pattern and size to be specified by owner |
| DJI Mic Mini transmitter/receiver with USB connection | 1 set for voice | [DJI Mic Mini](https://www.dji.com/mic-mini) — transmitter/receiver kit |
| Robot audio output or approved speaker | 1 route for voice | [Speaker catalog](https://www.logitech.com/en-us/shop/c/speakers) — interface/model to specify |
| Spare battery and approved charging/storage accessories | As needed | [Go2 battery](https://shop.unitree.com/products/go2-battery) · [charger](https://shop.unitree.com/products/unitree-go2-charger) — match delivered variant |
| Extra logging and backup storage | As needed | [Storage reference](../getting-started/hardware.md#workstation-specification-for-vla-pipeline-and-self-improvement-learning) |

The manipulation handoff must record the D435 clamp position and calibration target. For a voice-equipped station, verify the USB microphone connection and audio output during setup. Size spare batteries and storage for the session length and recording volume.

Microphones and speakers are task-specific accessories; a Quest headset is not part of this platform's core equipment. Complete the D1 mounting, calibration, and supervised checks before using the arm.

## 3. Understand the connections

<div class="connection-map" markdown="1">
<div class="connection-hub" markdown="1">

**Shared workstation → approved network → onboard computer**

The desktop stays at the desk; the onboard computer rides on the Go2.

</div>
<div class="connection-branches" markdown="1">
<div class="connection-branch" markdown="1">

**Onboard connections**

- Front D435i → USB data → onboard computer
- Go2 control → delivered robot interface
- Optional microphone → approved USB connection

</div>
<div class="connection-branch connection-branch--pending" markdown="1">

**D1 arm and added wrist camera**

- Arm power and Ethernet → expansion dock, per Unitree guide
- D435 wrist-camera USB host and cable route
- Stop control and recovery procedure

</div>
</div>
</div>

Use [Unitree’s connection diagram](https://support.unitree.com/home/en/developer/Payload) for the arm power and Ethernet cables. The added wrist camera’s USB host and cable route still need to be recorded; complete [D1 readiness](d1-arm.md) before use.

1. **Identify:** record the Go2 EDU Plus serial, battery, controller, and D1 package.
2. **Mount:** have the installer check the approved arm and camera mounts, gantry attachment, and clearance.
3. **Connect:** follow the delivered power/control instructions. Connect the front D435i to the onboard computer; connect the D1 using Unitree’s diagram and the wrist camera using its confirmed USB arrangement.
4. **Label:** mark both ends of camera and network cables. Photograph the ports for the private setup notes.
5. **Inspect:** check cable slack around the legs, wrist, and gripper before powered checks.

**Check before continuing:** the robot and desk computers are clearly distinguished, both cameras are identified, and the installer has approved the D1 connections. Before a walking test, manage any network tether according to the operator's procedure.

## 4. Check the delivered package

- [ ] Robot edition and control interface match the intended platform.
- [ ] Protective gantry and its attachment parts are present; the supplier has confirmed suitability for the Go2 with its mounted D1 and accessories.
- [ ] Onboard computer model, architecture, storage, power, and connections are documented.
- [ ] Battery, charger, controller, and stop procedure are available.
- [ ] Camera model, USB cable, mount, and selected image source agree.
- [ ] Access to the shared workstation and its network connection is arranged.
- [ ] Network connections and accessory mounts are ready.
- [ ] D1 arm, gripper, mounting kit, and power/data cables are included; calibration and stop procedures are recorded.
- [ ] Task-specific camera, voice, and storage accessories are listed separately.

**Next:** review [D1 arm readiness](d1-arm.md), then complete the [platform readiness checklist](readiness.md).
