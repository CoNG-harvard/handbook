# Equipment references

Use the manufacturer's instructions for the exact delivered model when mounting, connecting, powering, or servicing equipment. The handbook provides an equipment checklist and explains the layout; it does not replace model-specific electrical or mechanical instructions.

Each hardware table includes a **Product or reference** column. Product pages identify named equipment; **catalog** links provide options for generic supplies. A reference link does not confirm that a part is included or compatible with a custom mount.

## Manufacturer and supplier references

| Equipment | Reference | Use it for |
|---|---|---|
| xArm robots and control boxes | [UFACTORY installation guide](https://docs.xarm.ufactory.cc/2.hardware_installation.html) and [xArm product family](https://www.ufactory.cc/xarm-collaborative-robot/) | Confirming the arm model and supplied installation requirements |
| Quest headsets | [Meta Quest 3](https://www.meta.com/quest/quest-3/) | Headset, controller, and accessory identification |
| Go2 | [Unitree Go2](https://www.unitree.com/go2/) | Confirming the delivered robot edition and package with the supplier |
| D1 arm and mounting package | [D1 — US Robot Store](https://www.usrobotstore.com/products/unitree-go2-servo-robotic-arm-d1) | Confirming the D1 variant, gripper, Go2 mounting parts, and cables |
| Go2 battery, charger, and controller | [Battery](https://shop.unitree.com/products/go2-battery) · [charger](https://shop.unitree.com/products/unitree-go2-charger) · [controller](https://shop.unitree.com/products/go2-controller) | Matching accessories to the delivered Go2 |
| Onboard Jetson | [NVIDIA Jetson modules](https://developer.nvidia.com/embedded/jetson-modules) | Identifying the installed module; carrier board and memory still need confirmation |
| Go2 protective gantry | [RobotShop product listing](https://www.robotshop.com/products/unitree-go2-protective-bracket-gantry-go2-edu) | Identifying the Go2 EDU support frame and package; confirm suitability with the mounted D1 |
| D1 wrist camera mount | [RichBird C-clamp mount, 60 mm](https://www.amazon.com/dp/B0GSR6883N) | Project-owner-selected D435 mount; identifying the clamp, ball head, and camera screw |
| RealSense cameras | [D405](https://www.realsenseai.com/product-family/d405-series/) · [D435](https://www.realsenseai.com/products/stereo-depth-camera-d435/) · [D435i](https://www.realsenseai.com/products/depth-camera-d435i/) | Matching camera models to wrist and scene positions |
| RTX PRO 6000 | [NVIDIA workstation GPU family](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/) | Specifying the Blackwell Workstation Edition with 96 GB |
| CPU reference | [AMD Ryzen 9 7950X](https://www.amd.com/en/products/processors/desktops/ryzen/7000-series/amd-ryzen-9-7950x.html) | Identifying the reference processor |
| SSD reference | [WD_BLACK SN850X](https://www.sandisk.com/en-us/products/ssd/internal-ssd/wd-black-sn850x-nvme-ssd) | Selecting the recorded 2 TB capacity; confirm heatsink variant |
| DJI Mic Mini | [DJI product page](https://www.dji.com/mic-mini) | Identifying the transmitter/receiver kit for voice input |
| ABC Box | [I2RT product and package information](https://i2rt.com/products/abc-box) | Distinguishing the full Box from the Research Kit and checking included parts |
| ABC camera arrangement | [ABC assembly guide](https://abc.bot/hardware.html) | Understanding the separate build-your-own station; confirm details against the delivered Box instructions |

For the D1 arm, obtain the unit's manufacturer manual and the project owner's approved Go2 mounting plan. Exact fasteners, payload limits, wiring, and calibration details remain to be supplied for this platform.

## Basis for the equipment lists

- **Lab inventory, 24 September 2026:** the arm workstation inventory reported the selected RTX PRO 6000 and CPU/memory/storage reference. VLA Pipeline's current camera list follows the project owner's correction: two D405 wrist cameras and three D435 scene cameras. Connected-device counts do not establish the completeness of mounts, cables, or other accessories.
- **Project-owner requirements:** two xArm robots; a Go2 with D1 arm; one RTX PRO 6000 desktop shared by all three projects; and ABC Box as a separate platform with its own equipment list.
- **Supplied photographs:** the xArm and ABC Box photographs show visible arm and camera arrangements. The [Go2 platform PDF](../unidog-nav/assets/platform.pdf) identifies the Go2, D1 arm, and front D435i. The project owner confirmed the additional D1 wrist camera is a D435. Hidden parts and precise rig identities still require inspection.
- **Supplier information:** ABC package details were reviewed on 24 September 2026. Confirm the current order and delivered packing list before purchasing additional parts.

## Parts needing a final specification

The hardware tables link these items to relevant catalogs or assembly guidance. Exact purchase links still depend on the owner's build details:

- **Shared computer:** complete system, motherboard, RAM modules, power supply, case/cooling, HDD model, backup device, peripherals, and network equipment.
- **VLA Pipeline:** custom stands, gripper fingers/adapters, camera mounts, cable lengths, and task objects.
- **Go2/D1:** Jetson module/carrier board, D1 mounting kit, front-camera mount, accessory power, calibration target pattern/size, and speaker.
- **ABC Box:** leader variant, supplied control interfaces, and any parts missing from the delivered kit.

## Outstanding physical checks

The exact Go2 edition, onboard Jetson model, D1 installation details, custom xArm mounts/adapters, and complete ABC accessory package need owner or supplier confirmation. The project owner confirmed that all three projects share the same desktop. Each platform's physical connections and readiness checks still need to be verified at the station.

No robot or camera was operated during the handbook update. Hardware readiness must be checked and recorded by the installer and operator at the actual station.

For earlier lab material, see [Lab resources](lab-resources.md).
