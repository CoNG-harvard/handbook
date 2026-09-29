---
hide:
  - footer
---

# Glossary

Hardware and software terms used throughout the setup guides.

| Term | Meaning |
|---|---|
| Workstation | The shared computer with the RTX PRO 6000 GPU. Written as "workstation" everywhere in these guides |
| Driver | Software that lets the operating system communicate with a device |
| Firmware | Software stored inside a device, such as a robot control box or camera |
| SDK | A manufacturer's software toolkit for communicating with its equipment |
| Python environment | A separate folder of software packages, so one tool's installation does not change another's |
| ADB | Android Debug Bridge, a tool used to check a Quest headset's USB connection |
| ROS 2 | Software used to exchange robot sensor readings and commands; computers must use compatible releases and network settings |
| Topic / namespace | A named stream of ROS data / a prefix used to group names, for example by robot |
| LiDAR | A laser distance sensor that measures the surroundings |
| Odometry | A robot's estimate of its movement, often derived from its wheels |
| Motion capture / rigid body | External tracking of markers / a fixed arrangement of markers tracked as one object |
| Onboard computer | A computer carried by the robot; the Go2 EDU Plus includes one |
| Control box | The unit that connects an xArm to its power and control cables and carries its stop button |
| Gripper | The device at the end of an arm that holds objects |
| Finger | A replaceable contact piece on a gripper; the xArm fingers are 3D-printed in the lab |
| Wrist camera | A camera mounted near the gripper that moves with the arm |
| Scene camera | A camera on a fixed stand that looks at the wider work area |
| Leader / follower | An arm the operator moves by hand / an arm that copies that movement. A **passive** leader only measures position; a **powered** leader has motors and its own power supply |
| CAN | A wired communication link used by the ABC Box arms. Each arm needs a CAN connection to a computer, usually through a small USB adapter |
| Expansion dock | The mounting and connection area on the Go2's back, with a rail for accessories and power and Ethernet ports for the arm |
| Payload | Any accessory mounted on the Go2, such as the D1 arm or a camera |
| Gantry | A protective frame the Go2 stands inside during posture and movement tests |
| Calibration | Measurements that relate device positions, such as where a camera sits relative to an arm |
| Commissioning | The installer's and operator's checks before equipment is put into use |
| Home position | A predefined resting pose for an arm; check it against the actual mounting before the first reset |
| Data-capable USB cable | A USB cable that carries data as well as power; some charging cables do not |
| Project owner | The lab member responsible for a platform; supplies manuals, approvals, and access |
| Installer | The person who mounts and connects equipment and approves the physical installation |
| Operator | An experienced user who demonstrates stops, poses, and recovery and signs off the first session |
| Rig A / rig B | The two xArm robots and their matching control boxes. **Left / right** name the ABC Box leader/follower pairs |

[Return to Before you begin](index.md) · [All projects](../index.md)
