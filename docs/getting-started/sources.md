---
hide:
  - footer
---

# Equipment references

Use the manufacturer's instructions for the delivered model when mounting, connecting, powering, or servicing equipment. These guides list and explain the equipment; they do not replace model-specific electrical or mechanical instructions.

In every equipment table, a **product** link identifies a named model, a **catalog** link offers options for a generic supply, and a **reference** link points to assembly guidance. A link does not confirm that a part is included in a package or compatible with a custom mount; check sizes, compatibility, and included accessories before ordering.

## Manufacturer and supplier references

| Equipment | Reference | Use it for |
|---|---|---|
| xArm robots and control boxes | [UFACTORY installation guide](https://docs.xarm.ufactory.cc/2.hardware_installation.html) · [xArm product family](https://www.ufactory.cc/xarm-collaborative-robot/) | Arm model and installation requirements |
| xArm arm stands | [Vention design 506323](https://vention.com/machine-builder/506323) | The two stands; a Vention account with design access is required |
| xArm gripper fingers | [Finger STL](../vla-pipeline/assets/xarm-gripper-finger.stl) | Lab-designed 3D-print file; two fingers per gripper |
| xArm wrist-camera mount | [UFACTORY camera stand](https://www.ufactory.us/product/ufactory-xarm-camera-stand) | Mount for the two D405 wrist cameras |
| xArm scene-camera clamps | [CAMVATE C-clamp](https://www.amazon.com/dp/B0BYDH27WQ) · [CAMVATE screw adapters](https://www.amazon.com/dp/B0DQNP61JC) | Threaded C-clamps and screw adapters for the scene-camera supports; adjustable heads are separate |
| xArm task tubs | [Rubbermaid 7-gallon utility box](https://www.amazon.com/dp/B000BC5EP8) | The gray tubs on the station table |
| Quest headsets | [Meta Quest 3](https://www.meta.com/quest/quest-3/) | Headset, controller, and accessory identification |
| Go2 EDU Plus | [Unitree Go2](https://www.unitree.com/go2/) | Robot edition and included accessories |
| D1 arm and mounting | [Unitree payload installation](https://support.unitree.com/home/en/developer/Payload) · [D1 supplier](https://www.usrobotstore.com/products/unitree-go2-servo-robotic-arm-d1) | Official rail mounting and arm power/Ethernet connections |
| Go2 battery, charger, and controller | [Battery](https://shop.unitree.com/products/go2-battery) · [charger](https://shop.unitree.com/products/unitree-go2-charger) · [controller](https://shop.unitree.com/products/go2-controller) | Matching accessories to the delivered Go2 |
| Go2 protective gantry | [RobotShop listing](https://www.robotshop.com/products/unitree-go2-protective-bracket-gantry-go2-edu) | The Go2 EDU support frame; SKU RB-Unt-97, part Go2-Protective-Bracket |
| D1 wrist-camera mount | [RichBird C-clamp mount](https://www.amazon.com/dp/B0GSR6883N) | Clamp, ball head, and 1/4"-20 screw for the D435 wrist camera |
| RealSense cameras | [D405](https://www.realsenseai.com/product-family/d405-series/) · [D415](https://www.realsenseai.com/products/stereo-depth-camera-d415/) · [D435](https://www.realsenseai.com/products/stereo-depth-camera-d435/) · [D435i](https://www.realsenseai.com/products/depth-camera-d435i/) | Matching camera models to wrist, scene, and front positions |
| RTX PRO 6000 | [NVIDIA RTX PRO 6000 family](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/) | The Blackwell Workstation Edition with 96 GB |
| CPU and SSD (reference machine) | [AMD Ryzen 9 7950X](https://www.amd.com/en/products/processors/desktops/ryzen/7000-series/amd-ryzen-9-7950x.html) · [WD_BLACK SN850X](https://www.sandisk.com/en-us/products/ssd/internal-ssd/wd-black-sn850x-nvme-ssd) | Identifying the existing workstation's parts |
| DJI Mic Mini | [DJI product page](https://www.dji.com/mic-mini) | Transmitter/receiver kit for voice input |
| ABC Box | [I2RT package information](https://i2rt.com/products/abc-box) · [I2RT hardware reference](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md) | Package contents, leader options, and interfaces |
| ABC camera arrangement | [ABC assembly guide](https://abc.bot/hardware.html) | The build-your-own station that the camera layout follows |
| TurtleBot3 Burger | [ROBOTIS kit contents](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/#components) · [assembly](https://emanual.robotis.com/docs/en/platform/turtlebot3/hardware_setup/) · [setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/) | Matching the delivered robot, parts, and software versions |
| Optional OptiTrack system | [Rigid-body tracking](https://docs.optitrack.com/motive/rigid-body-tracking) · [streaming](https://docs.optitrack.com/motive/data-streaming) | Marker setup and external position data |
| Consumables and tools | [Zip ties](https://www.amazon.com/dp/B08TVLYB3Q) · [AA batteries](https://www.amazon.com/dp/B00NTCH52W) · [M4 screw kit](https://www.amazon.com/dp/B0GS8BT7XL) · [hex key set](https://www.amazon.com/dp/B0776C2D6H) · [digital angle gauge](https://www.amazon.com/dp/B0D65VNWPH) | Cable management, Quest controllers, D1 rail screws, and assembly |

## Basis for the equipment lists

The lists combine the project owner's platform requirements, the available station photographs, the lab's purchase record, and the manufacturers' package lists. Photographs establish only visible equipment; package inclusions come from supplier lists. Cable lengths and hidden connections still need checking on the station. Serial numbers and network addresses stay in the private station record.

## Open items

Resolve these with the owner or supplier before the step that needs them.

**Shared workstation**

- Complete build for a new computer: motherboard, memory modules, power supply, case and cooling, HDD model, backup device.

**VLA Pipeline**

- Models of the three articulated scene-camera stands and their adjustable camera heads.
- Pending camera cables have Micro-B USB 3.0 connectors; the D405 and D415 have USB Type-C ports. Confirm the intended camera or adapter before connecting them.
- Any gripper adapter needed beyond the printed fingers.
- Print settings and fit check for the gripper fingers.
- Work table size and load rating, black tray model, and task objects.

**Self Improvement Learning**

- USB host and cable route for the D435 wrist camera.
- Design file for the printed D435i head bracket, and whether it replaces Unitree's official D435i mount.
- Gantry clearance and load with the D1 mounted.
- Calibration target pattern and size; accessory power; speaker.

**ABC Box**

- Delivered variant (Box or Research Kit), packing list, and matching power supplies and power cords.
- Leader model (passive GELLO or powered YAM) and its power and calibration procedure.
- Which computer receives each camera and arm interface, and how many external CAN adapters are needed.
- Stop arrangement: what it cuts and how to recover.

**TurtleBot3 Burger**

- Fleet size and installed Raspberry Pi and LiDAR revisions; hardware quantities in the guide are per robot.
- Current OS/ROS versions and the host for the matching operator environment.
- A station photograph for the overview.
- If OptiTrack is used: the installed room configuration, Motive version, receiving computer, and maintained pose bridge.

[All projects](../index.md)
