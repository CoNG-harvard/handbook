# Before you begin

**Goal:** choose a platform, gather its equipment, and arrange help for assembly and the first powered checks. No prior robotics experience is needed to use these guides. Unfamiliar terms are explained in the [glossary](glossary.md).

## 1. Choose a project

| Project | Physical setup | Computer |
|---|---|---|
| [VLA Pipeline](../vla-pipeline/index.md) | Two xArm 7 robots, grippers, five cameras, and Quest headsets | Shared workstation |
| [Self Improvement Learning](../unidog-nav/index.md) | Unitree Go2 EDU Plus, D1 arm, D435i front camera, D435 wrist camera, and onboard computer | Shared workstation plus the robot's onboard computer |
| [ABC Box](../abc-box/index.md) | Two follower arms, two leader arms, and three cameras | Shared workstation plus the included Box PC |
| [TurtleBot3 Burger](../turtlebot3/index.md) | Wheeled robot, LiDAR, and optional OptiTrack markers | Matching ROS environment plus the onboard Raspberry Pi |

Use the [shared hardware list](hardware.md) for the workstation and its accessories.

## 2. Arrange the setup handover

Ask the project owner for:

- The packing list and manufacturer manuals for the delivered models.
- Approved mounts, fasteners, cables, power supplies, and the planned layout.
- A named installer and an experienced operator for the first powered checks.
- A demonstration of the stop controls, power-on sequence, and shutdown procedure.
- Existing calibration records and a place to keep the station's equipment record.

Check quantities before assembly. Resolve missing or unspecified parts with the owner or supplier before the step that needs them. All [open items](sources.md#open-items) are listed in one place.

## 3. Prepare the work area

Use a stable surface and the manufacturer's mounting instructions. Arrange lighting and camera views, leave room around moving parts, and keep cables clear of joints and walkways. Have the installer confirm power requirements before connecting equipment.

Read the [safety rules](safety.md) before enabling motion on any platform.

## 4. Follow the setup sequence

For VLA Pipeline, Self Improvement Learning, and ABC Box, prepare the shared workstation and its [basic software](software.md) once. For TurtleBot3, follow its [matching ROS environment](../turtlebot3/software.md#1-choose-the-matching-environment) instructions. For your project, follow **equipment and connections → basic software → hardware readiness**, including the D1 mounting step for the Go2. Each software page identifies the computer to use and the expected result.

## 5. Keep setup notes

Record device models, serial numbers, cable labels, camera positions, network addresses, calibration dates, and the responsible operator in a private setup sheet. Use the same labels on the equipment and in the record: **rig A** and **rig B** for the xArm robots, **left** and **right** for the ABC Box pairs, and **front**, **wrist**, **scene**, and **overhead** for cameras. Give each TurtleBot3 a distinct robot label. Do not publish serials or network addresses.

**Next:** [Shared computer and hardware](hardware.md)
