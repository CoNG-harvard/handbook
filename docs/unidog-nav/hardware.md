---
title: Self Improvement Learning hardware
---

# Self Improvement Learning hardware

**Goal:** assemble the platform — one Go2 EDU Plus with one D1 arm, two cameras, and the control equipment — and connect it to the [workstation](../getting-started/hardware.md).

[Identify the parts in the labeled photograph](index.md).

## 1. Equipment

Workstation, display, and network equipment are counted once in [shared equipment](../getting-started/hardware.md#shared-equipment).

| Equipment | Quantity | Product or reference |
|---|---|---|
| Unitree Go2 EDU Plus with onboard computer | 1 | [Unitree Go2](https://www.unitree.com/go2/) |
| Go2 protective gantry | 1 | [RobotShop listing](https://www.robotshop.com/products/unitree-go2-protective-bracket-gantry-go2-edu) — SKU RB-Unt-97, part Go2-Protective-Bracket; one per package |
| Unitree D1 arm with gripper | 1 | [D1 arm — US Robot Store](https://www.usrobotstore.com/products/unitree-go2-servo-robotic-arm-d1) |
| D1 mounting kit and power/Ethernet cables | 1 set | [Unitree payload installation](https://support.unitree.com/home/en/developer/Payload) — section **Installing the Small Servo Arm** |
| Spare M4 screws for the D1 rail | 1 kit | [M4 hex screw kit, 6–30 mm](https://www.amazon.com/dp/B0GS8BT7XL) — Unitree specifies M4 × 10 |
| Go2 battery and charger | 1 set | [Battery](https://shop.unitree.com/products/go2-battery) · [charger](https://shop.unitree.com/products/unitree-go2-charger) |
| Go2 controller with stop function | 1 | [Go2 controller](https://shop.unitree.com/products/go2-controller) |
| RealSense D435i front camera with USB cable | 1 | [D435i](https://www.realsenseai.com/products/depth-camera-d435i/) · [USB cable catalog](https://www.startech.com/en-us/cables/usb-30) |
| D435i head bracket | 1 | 3D-printed, vented — design file to record; see [open items](../getting-started/sources.md#open-items) |
| RealSense D435 wrist camera with USB cable | 1 | [D435](https://www.realsenseai.com/products/stereo-depth-camera-d435/) · [USB cable catalog](https://www.startech.com/en-us/cables/usb-30) |
| D1 wrist-camera clamp mount | 1 | [RichBird 60 mm C-clamp with ball head](https://www.amazon.com/dp/B0GSR6883N) — 1/4"-20 camera screw |
| Robot network connection | 1 | [Ethernet cable catalog](https://www.startech.com/en-us/cables/network) — wired or the lab's wireless arrangement |
| Accessory power, mounts, and cable restraints | As needed | [Unitree accessories](https://shop.unitree.com/collections/all) · [zip ties](https://www.amazon.com/dp/B08TVLYB3Q) |
| Clear test area with floor markings | 1 | [Floor-marking tape catalog](https://www.mcmaster.com/products/floor-marking-tape/) |

### Task-specific accessories

| Equipment | Quantity | Product or reference |
|---|---|---|
| Manipulation calibration target | 1 | [Calibration-target example](https://calib.io/products/kalibr-targets) — pattern and size set by the owner |
| DJI Mic Mini transmitter/receiver | 1 set | [DJI Mic Mini](https://www.dji.com/mic-mini) — for voice input |
| Speaker or robot audio output | 1 | [Speaker catalog](https://www.logitech.com/en-us/shop/c/speakers) — model to specify |
| Spare battery | As needed | [Go2 battery](https://shop.unitree.com/products/go2-battery) |
| Extra recording storage | As needed | [Shared storage](../getting-started/hardware.md#shared-equipment) |

### Notes on selection

- **Robot:** the Go2 EDU Plus package includes the onboard computer and a built-in front camera. The D435i is a separate, added camera; confirm which one a session uses.
- **Gantry:** an external frame for posture and movement tests. Check its attachment, load rating, and clearance with the D1 mounted.
- **D1 arm:** mounts on the Go2 expansion dock rail with square nuts and M4 × 10 hex-socket screws, and connects to the dock's power and Ethernet ports. Follow [Unitree's guide](https://support.unitree.com/home/en/developer/Payload) and then [Mount and check the D1 arm](d1-arm.md).
- **Cameras:** the D435i sits in a 3D-printed vented bracket on the Go2's head; [Unitree's payload guide](https://support.unitree.com/home/en/developer/Payload) also describes the official front D435i installation. The D435 clamps beside the gripper with the [RichBird mount](https://www.amazon.com/dp/B0GSR6883N). Leave cable slack and clearance around the gripper.
- **Accessories:** a Quest headset is not part of this platform. For a voice-equipped session, check the USB microphone and audio output during setup. Size spare batteries and storage for the session length.

## 2. Connection map

<div class="connection-map" markdown="1">
<div class="connection-hub" markdown="1">

**Workstation → lab network → Go2 onboard computer**

The workstation stays at the desk; the onboard computer rides on the Go2.

</div>
<div class="connection-branches" markdown="1">
<div class="connection-branch" markdown="1">

**Onboard connections**

- Front D435i → USB → onboard computer
- Go2 controller → Go2, as delivered by Unitree
- Microphone (optional) → USB

</div>
<div class="connection-branch connection-branch--pending" markdown="1">

**D1 arm and wrist camera — to confirm**

- Arm power and Ethernet → expansion dock, per Unitree's diagram
- D435 wrist camera → USB host and cable route to record

</div>
</div>
</div>

The dashed box needs the arm's connection details recorded before use.

## 3. Assemble and connect

1. **Identify:** record the Go2 serial, battery, controller, and D1 package against the packing list.
2. **Mount:** fit the D435i bracket to the head and assemble the gantry per its instructions. Mount the D1 and its wrist camera by following [Mount and check the D1 arm](d1-arm.md).
3. **Connect:** plug the D435i into the onboard computer; connect the D1's power and Ethernet to the dock per Unitree's diagram; route the wrist-camera USB cable to its confirmed host.
4. **Label:** mark both ends of every camera and network cable. Photograph the ports for the setup notes.
5. **Inspect:** check cable slack around the legs, arm joints, wrist, and gripper before powered checks.

## 4. Record identities

| Item | What to record |
|---|---|
| Go2 and onboard computer | Serials, edition, and network connection method |
| D1 arm | Serial, mounting position, and cable routing |
| Cameras | Serial, mounting position, and USB host for the D435i and the D435 |
| Battery and controller | Identities and the demonstrated stop procedure |

**Next:** [Mount and check the D1 arm](d1-arm.md)
