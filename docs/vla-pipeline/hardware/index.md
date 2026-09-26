---
title: VLA Pipeline hardware
---

# VLA Pipeline hardware

**Goal:** identify and connect the two-arm VLA Pipeline station. It has **two xArm 7 robots**, each with its own control box, gripper, and mounting stand. Both use the workstation shared with Self Improvement Learning and ABC Box. Check rig A first, then rig B, before using both together.

[Identify the parts in the labeled photograph](../index.md) — both xArm robots, two D405 wrist cameras, and three D435 scene cameras.

## 1. Gather the equipment

Quantities below describe the **two-arm lab station**. The [shared workstation, GPU, display/input devices, and network equipment](../../getting-started/hardware.md#shared-equipment-prepare-once) are shared by all three projects and counted once. The full station allows two headsets, each with two controllers. **One operator can control both arms with one headset and its controller pair** in the two-arm arrangement supported by the lab reference. Confirm the arrangement for the first session with the project owner.

Product links identify known models. **Catalogs** and assembly **references** cover unspecified parts; confirm exact sizes, compatibility, and included accessories before ordering.

| Equipment | Quantity | Product or reference |
|---|---|---|
| UFACTORY xArm 7 robot | 2 | [UFACTORY xArm](https://www.ufactory.cc/xarm-collaborative-robot/) — select xArm 7 |
| Matching control box and cable/power set | 2 sets | [Control box and supplied cables](https://docs.xarm.ufactory.cc/2.hardware_installation.html) — installation reference |
| Compatible xArm gripper and mounting/cable set | 2 sets | [UFACTORY grippers](https://www.ufactory.cc/solution-pickandplace/) — reference; lab fingers/adapters to specify |
| Rigid arm mount or stand | 2 | [Base mounting requirements](https://docs.xarm.ufactory.cc/2.hardware_installation.html) — custom stand drawing needed |
| Shared work table | 1 | [Workbench catalog](https://www.mcmaster.com/products/workbenches/) — size/load rating to specify |
| Meta Quest 3 headset | 2 for the full station; 1 for one-operator, two-arm use | [Meta Quest 3](https://www.meta.com/quest/quest-3/) |
| Quest controller | 2 per headset; 4 for the full station | [Touch Plus controllers](https://www.meta.com/quest/accessories/quest-touch-plus-controller/) — two pairs; check headset bundle |
| Headset USB data cable | 1 per headset used; up to 2 | [Meta Link cable](https://www.meta.com/quest/accessories/link-cable/) — cable reference; equivalent data cable allowed |
| RealSense D405 wrist camera, bracket, and USB cable | 2 sets | [D405](https://www.realsenseai.com/product-family/d405-series/) · [USB cable catalog](https://www.startech.com/en-us/cables/usb-30) — wrist mount listed below |
| RealSense D435 scene camera, stand, and USB cable | 3 sets | [D435](https://www.realsenseai.com/products/stereo-depth-camera-d435/) · [USB cable catalog](https://www.startech.com/en-us/cables/usb-30) — stand to specify |
| UFACTORY xArm wrist-camera mount | 2; one per D405 wrist camera | [UFACTORY camera stand](https://www.ufactory.us/product/ufactory-xarm-camera-stand) — D405 fit confirmed by project owner |
| Arm-controller-to-switch Ethernet cable | 2 | [Ethernet cable catalog](https://www.startech.com/en-us/cables/network) |
| Task objects and tray/basket | 1 task set | [Tray catalog](https://www.mcmaster.com/products/trays/) — task objects chosen by project owner |
| Cable labels, cable management, and suitable lighting | As needed | [Labels](https://www.mcmaster.com/products/labels/) · [cable ties](https://www.mcmaster.com/products/cable-ties/) · [lighting](https://www.mcmaster.com/products/work-lights/) — catalogs |

### Photo count check

The current photo shows **2 arms, 2 wrist cameras, and 3 scene cameras**: **5 cameras total**, matching the list. The earlier view also shows **2 grippers, 2 arm stands, 2 control boxes with stop buttons, and 2 headsets**. The controller illustration shows one pair; it does not verify the listed four controllers. Confirm loose cables and accessories against the station inventory.

### Selection details

- **Arms and controllers:** match the lab's [xArm 7](https://www.ufactory.cc/xarm-collaborative-robot/). Confirm included power supplies, mains leads, and arm/controller cables against [UFACTORY's installation guide](https://docs.xarm.ufactory.cc/2.hardware_installation.html).
- **Grippers and stands:** obtain the approved finger geometry, adapters, calibration, base plates, and fasteners from the owner. Exact custom part numbers and the stand bill of materials remain to be specified.
- **Headsets:** include [Quest 3](https://www.meta.com/quest/quest-3/) chargers, controller batteries, and data-capable USB cables long enough for the operator.
- **Cameras:** use one [D405](https://www.realsenseai.com/product-family/d405-series/) per wrist and three [D435 scene cameras](https://www.realsenseai.com/products/stereo-depth-camera-d435/) for the full station. Confirm mounting, view, and USB bandwidth before using all five.
- **Wrist-camera mounts:** use one [UFACTORY xArm camera stand](https://www.ufactory.us/product/ufactory-xarm-camera-stand) per D405 wrist camera. The project owner confirmed the D405 fit. The listing names D435 and includes a mounting plate and 2 m USB-C cable; the camera is separate. Count these mounts within the two wrist-camera sets above to avoid ordering duplicate brackets or cables.
- **Network and task area:** the workstation cable and switch are counted in [shared equipment](../../getting-started/hardware.md#shared-equipment-prepare-once). Choose objects and camera positions for the intended task; keep cables away from moving joints.

Both arms' stop controls must be accessible and clearly labeled. Confirm which button stops which arm before powering or resetting either robot.

### Camera configuration and optional accessories

The project owner confirmed **2 D405 wrist cameras**; the station also has **3 D435 scene cameras**. Record their serial numbers and physical positions before the first session. A first test can use just rig A's wrist and scene views; enable the remaining cameras as you validate the full station.

Both arms belong to the platform even when only one is used for the first check. Extra [storage](https://www.westerndigital.com/products/hdd/internal-hdd), soft fingers, [gripping tape](https://www.mcmaster.com/products/grip-tape/), and custom adapters depend on the task; confirm their exact specifications with the owner.

## 2. Mount and wire the station

### Connection map

<div class="connection-map" markdown="1">
<div class="connection-hub" markdown="1">

**Shared workstation** · RTX PRO 6000

</div>
<div class="connection-branches" markdown="1">
<div class="connection-branch" markdown="1">

**Ethernet → shared switch/router**

- Control box A → supplied arm cables → xArm A
- Control box B → supplied arm cables → xArm B

</div>
<div class="connection-branch" markdown="1">

**USB data → workstation**

- 2 × D405 wrist cameras
- 3 × D435 scene cameras
- Each Quest headset used for the session

</div>
</div>
</div>

This map shows data connections. Each control box also needs its matching mains lead; connect power and arm cables using [UFACTORY's installation instructions](https://docs.xarm.ufactory.cc/2.hardware_installation.html). Identify the delivered controller's ports before attaching cables. Disconnect external AC before connecting or disconnecting arm cables.

### Assemble and connect

1. **Mount:** secure both arm bases and grippers using the approved drawings and fasteners. Check the two arms' overlapping work area.
2. **Pair:** label arms and control boxes **A** and **B**. Attach each arm's supplied power and communication cables to its matching box.
3. **Network:** connect both control boxes and the workstation to the shared switch/router with Ethernet.
4. **Cameras:** mount one D405 per wrist and three D435s on stable stands. Label both ends of each USB cable with its camera position, then connect to the workstation.
5. **Headsets:** connect each headset used for the session with a data-capable USB cable. Keep its controllers together.
6. **Inspect:** have the installer check connections and cable clearance before power-on. Photograph the ports and cable labels for the [station record](../../getting-started/station-record.md).

**Check before continuing:** two arm/control-box pairs, five labeled camera cables, stable mounts, and accessible stop controls. An operator checks rig A and rig B separately before a combined session.

A network switch adds wired connections; it does not necessarily assign IP addresses. Ask the person setting up the network to make the arm controller and workstation reachable on the same network. Keep the addresses in your private setup note.

## 3. Identify the arm and stop control

Label the robots **rig A** and **rig B**. Record each arm's IP address, and label its matching control box and stop button. Do not infer rig identity from left/right position in the photograph.

Ask the operator to demonstrate stopping, restoring power, and returning to the home position. A **home position** is a predefined pose; the lab's home angles must be checked against your mounting arrangement before the first reset.

## 4. Record device identities

Keep separate records for rig A and rig B. Match each physical device with its cable label and its intended role.

| Item | What to record |
|---|---|
| Arm and control box | Model, serial, network address, and matching stop control |
| Headset and controllers | Device identities and arm assignments; record if one headset controls both arms |
| Wrist cameras | Serial number and assigned arm; one camera per wrist |
| Scene cameras | Serial number, stand position, and intended view for each of the three cameras |
| Workstation/network | Connection method, cable labels, and assigned addresses |

Ask the installer to confirm device identities. A label such as **rig A wrist** describes the camera's role; its serial identifies the physical unit. Keep actual network addresses in your private station record.

## 5. Identify the headset controls

<figure class="handbook-figure" markdown="1">

![Quest controllers labeled with trigger and grip/side-button positions.](../assets/quest_controllers.png)

<figcaption markdown="1">

Left controller: **X/Y** buttons. Right controller: **A/B** buttons, **trigger** (front), and **grip/side button**. The red callouts identify the trigger position and side button.

[View full-size image](../assets/quest_controllers.png)
{ .figure-links }

</figcaption>

</figure>

Keep each controller pair with its headset, and include charging leads and spare controller batteries in the station kit.

**Next:** [Check hardware readiness](../readiness.md).
