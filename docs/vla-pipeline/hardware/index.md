# VLA Pipeline hardware

**Goal:** identify and connect the two-arm VLA Pipeline station. It has **two xArm 7 robots**, each with its own control box, gripper, and mounting stand. Both use the workstation shared with Self Improvement Learning. Check rig A first, then rig B, before using both together.

<figure class="handbook-figure" markdown="1">

![Real lab photo labeled with the xArm, gripper, Quest headset, task objects, mounting stand, control boxes, and stop buttons.](../assets/system_overview-labeled.svg)

<figcaption markdown="1">

VLA Pipeline lab station with two xArm 7 robots. Validate each rig separately before using both together.

[View full-size image](../assets/system_overview-labeled.svg) · [Source photograph](../assets/system_overview.jpg)
{ .figure-links }

</figcaption>

</figure>

## 1. Gather the equipment

Quantities below describe the **two-arm lab station**. The [shared workstation, GPU, display/input devices, and network equipment](../../getting-started/hardware.md#shared-equipment-prepare-once) are counted once for both projects. Two independent operators use two headset sets; the one-headset, two-arm mode is a separate software configuration.

| Item and quantity | Why you need it | Selection notes |
|---|---|---|
| **2 UFACTORY xArm 7 robots** | Moves the gripper | Match the lab arm type and software; see [UFACTORY's xArm overview](https://help.ufactory.cc/en/articles/4491842-the-difference-between-ufactory-xarm5-ufactory-xarm6-and-ufactory-xarm7) |
| **2 matching control boxes**, each with arm/controller cables, power supply and mains lead | Powers and controls the arm | Check what is included in the robot package; follow [UFACTORY's hardware installation guide](https://docs.xarm.ufactory.cc/2.hardware_installation.html) |
| **2 compatible xArm grippers**, each with an adapter/mount and cable set | Grasps objects | Confirm the lab's finger/pad geometry and gripper calibration with the model owner; exact custom mount/soft-finger part numbers are not established here |
| **2 rigid arm mounting assemblies/stands**, with a shared work table | Holds the arm base securely | Base plate, mounting surface, and fasteners must be specified for this robot; the old notes do not provide a complete stand bill of materials |
| **2 Meta Quest 3 headsets + 4 controllers** | Tracks the operator's hand movement | One headset set per operator; include chargers and controller batteries; [Meta product reference](https://www.meta.com/quest/quest-3/) |
| **2 headset USB data cables** | Connects the headset page to the workstation | Must carry data, fit the ports, and allow comfortable operator movement |
| **2 RealSense D405 wrist cameras** | Shows the gripper and nearby object | One per arm, each with a wrist bracket and USB data cable; [D405 reference](https://www.realsenseai.com/product-family/d405-series/) |
| **3 RealSense D415 scene cameras** | Shows the whole work area | Three were connected in the inspected lab setup. Include stands/clamps and USB data cables; [camera family reference](https://www.realsenseai.com/products/) |
| **1 wired network connection per device** | Connects the arm controller and workstation | Provide 2 arm-controller-to-switch cables, one per control box; the workstation-to-switch cable is counted in the shared setup. Use the selected network design for any additional cables |
| **1 set of task objects and a tray/basket** (example task) | Provides the scene being recorded or manipulated | Use objects/camera positions appropriate for the model; a red-cube model is not a general-purpose object handler |
| **Cable management, labels, and suitable lighting** | Keeps connections identifiable and views usable | Route cables away from joints; maintain camera views and consistent lighting |

Both arms' stop controls must be accessible and clearly labeled. Confirm which button stops which arm before powering or resetting either robot.

### Camera configuration and optional accessories

The September 2026 USB inventory reported **2 D405 and 3 D415 cameras connected**. Record their physical positions and topic assignments before configuring recording. A first test can use just rig A's wrist and scene views; enable the remaining cameras as you validate the full station.

Rig B is optional in some software configurations, but the second arm is part of the lab's hardware setup. Extra storage, soft fingers, gripping tape, and custom adapters depend on the task and trained model; confirm their exact specifications with the owner.

## 2. Mount and wire the station

Have a qualified person mount the arm and gripper using the manufacturer's instructions for the exact hardware. This handbook does not specify mounting loads, bolt torque, electrical wiring, or firmware updates.

1. Secure both arm bases and grippers. Check each arm's movement area and where the two areas overlap.
2. Connect each arm to its matching control box using the supplied cables.
3. Connect both control boxes and the shared workstation to the same network using Ethernet.
4. Mount one wrist camera per arm and position the scene cameras for the intended views. Connect the cameras by USB to the shared workstation.
5. Connect each Quest used for the session to the workstation with its own **data-capable** USB cable.
6. Check cable slack for both arms before running a reset. Test each rig separately before combined operation.

A network switch adds wired connections; it does not necessarily assign IP addresses. Ask the person setting up the network to make the arm controller and workstation reachable on the same network. Keep the addresses in your private setup note.

## 3. Identify the arm and stop control

Label the robots **rig A** and **rig B**. Record each arm's IP address, and label its matching control box and stop button. Do not infer rig identity from left/right position in the photograph.

Ask the operator to demonstrate stopping, restoring power, and returning to the home position. A **home position** is a predefined pose; the lab's home angles must be checked against your mounting arrangement before the first reset.

## 4. Record device identities

Keep separate records for rig A and rig B. Camera topics and headset identities must match the selected rig configuration.

| Value to record | How you will use it |
|---|---|
| Arm IP address | `record.robot.xarm_ip` and `record.teleop.xarm_ip` |
| Workstation/camera-server address | `record.teleop.img_server_ip`; inference camera host |
| Headset serial | `rig.quest_serial` |
| Wrist camera serial | `rig.cameras.wrist_camera` |
| Scene camera serial | `rig.cameras.right_3pv_camera` |

The [software installation](../install.md) supplies the commands for discovering the headset and cameras. Do not confuse a camera's serial number with its **topic name**: `wrist_camera` is a software label for a camera; the serial identifies the physical device.

**Next:** [Install the arm software](../install.md).
