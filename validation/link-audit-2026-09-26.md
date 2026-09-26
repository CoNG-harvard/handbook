# Website link audit — 26 September 2026

Scope: all external anchor destinations extracted from the locally built website, including navigation/footer links and the newly supplied Vention stand design. Local pages, fragment targets, and linked assets were checked separately. This report is not published.

## Results

- 16 content pages: no missing internal destinations or fragment targets; all 51 hardware rows contain a product/reference link.
- 46 distinct external hyperlink destinations: 42 HTTP 200 responses, two HTTP 403 anti-bot responses, one HTTP 567 response, and one timeout.
- AMD and Unitree loaded correctly in the browser after their automated checks failed.
- Kingston and RobotShop showed browser verification pages; the expected content was retrievable through web browsing. These links are not demonstrated broken, but friction-free access is not confirmed.
- Vention requires sign-up/sign-in and design access. The design is now linked with that requirement stated; its contents were not verified.
- No HTTP 404 or 410 was found. A successful HTTP response alone does not guarantee product availability, compatibility, or unrestricted access from every location.
- Strict MkDocs build and whitespace checks passed.

## External destinations

| Destination | Automated result | Follow-up |
|---|---|---|
| [Assembly · ABC Docs](https://abc.bot/hardware.html) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Kalibr Targets – calib.io](https://calib.io/products/kalibr-targets) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [2. Hardware Installation / UFactory Docs](https://docs.xarm.ufactory.cc/2.hardware_installation.html) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [GitHub - CoNG-harvard/handbook · GitHub](https://github.com/CoNG-harvard/handbook) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [yam-abc-reproduce/docs/hardware.md at main · i2rt-robotics/yam-abc-reproduce · GitHub](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [ABC Box – I2RT Robotics](https://i2rt.com/products/abc-box) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Products – UnitreeRobotics](https://shop.unitree.com/collections/all) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Go2 Battery – UnitreeRobotics](https://shop.unitree.com/products/go2-battery) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Go2 Controller – UnitreeRobotics](https://shop.unitree.com/products/go2-controller) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Unitree Go2 Charger – UnitreeRobotics](https://shop.unitree.com/products/unitree-go2-charger) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [support.unitree.com](https://support.unitree.com/home/en/developer/Payload) | 567 | Opened the full Payload article in the browser; verified the small servo arm section. Command-line requests were blocked. |
| [Sign up / Vention](https://vention.com/machine-builder/506323) | 200 | Redirects to Vention sign-up. Account/design access required; the actual design contents were not inspected. |
| [Amazon.com: C-Clamp Mount with 360 Degree Ball Head & 1/4 Screw Adapter for Camera / Compatible with Go Pro, Ring, Google Nest, Wyze, and Arlo, Fits Desk/Railing/Branch/Handlebar, Metal, Black (60mm) : Patio, Lawn & Garden](https://www.amazon.com/dp/B0GSR6883N) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [www.amd.com](https://www.amd.com/en/products/processors/desktops/ryzen/7000-series/amd-ryzen-9-7950x.html) | 000 | Opened and confirmed the Ryzen 9 7950X page in the browser after command-line timeout. |
| [Monitors / Dell USA](https://www.dell.com/en-us/shop/pc-accessories/ar/computer-monitors) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [DJI Mic Mini - Carry Less, Capture More - DJI United States](https://www.dji.com/mic-mini) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Just a moment...](https://www.kingston.com/en/memory) | 403 | Browser stopped at an anti-bot check. The expected memory finder page was independently retrieved with web browsing; unrestricted browser access is not confirmed. |
| [Computer Keyboards - Wireless, Bluetooth, Mechanical / Logitech](https://www.logitech.com/en-us/shop/c/keyboards) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Computer Mice - Wireless Mouse, Bluetooth, Wired / Logitech](https://www.logitech.com/en-us/shop/c/mice) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Speakers - Bluetooth, Wireless & Surround Sound / Logitech United States](https://www.logitech.com/en-us/shop/c/speakers) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [McMaster-Carr](https://www.mcmaster.com/products/cable-ties/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [McMaster-Carr](https://www.mcmaster.com/products/floor-marking-tape/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [McMaster-Carr](https://www.mcmaster.com/products/grip-tape/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [McMaster-Carr](https://www.mcmaster.com/products/labels/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [McMaster-Carr](https://www.mcmaster.com/products/trays/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [McMaster-Carr](https://www.mcmaster.com/products/work-lights/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [McMaster-Carr](https://www.mcmaster.com/products/workbenches/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Quest Link Cable / Connect PC to VR Headset / Meta Quest / Meta Store](https://www.meta.com/quest/accessories/link-cable/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Quest 3 Meta Quest Touch Plus Controller / Meta Store](https://www.meta.com/quest/accessories/quest-touch-plus-controller/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Meta Quest 3: Next-Gen Virtual Reality Headset / Meta Store](https://www.meta.com/quest/quest-3/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [www.netgear.com](https://www.netgear.com/business/wired/switches/unmanaged/) | 200 | Confirmed the unmanaged-switch catalog in the browser. |
| [RTX PRO 6000 Blackwell Series / NVIDIA](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [D405 Series Archives - RealSense](https://www.realsenseai.com/product-family/d405-series/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [D435i - RealSense](https://www.realsenseai.com/products/depth-camera-d435i/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [D435 - RealSense](https://www.realsenseai.com/products/stereo-depth-camera-d435/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Just a moment...](https://www.robotshop.com/products/unitree-go2-protective-bracket-gantry-go2-edu) | 403 | Browser stopped at an anti-bot check. The expected Go2 gantry listing was independently retrieved with web browsing; unrestricted browser access is not confirmed. |
| [www.sandisk.com](https://www.sandisk.com/en-us/products/ssd/internal-ssd/wd-black-sn850x-nvme-ssd) | 200 | Confirmed the SN850X product family in the browser. Landing variant defaults to 1 TB; select the documented 2 TB capacity and required heatsink option. |
| [Network Cables & Adapters - Cables / StarTech.com](https://www.startech.com/en-us/cables/network) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [USB 3.0 Cables / Cables - Cables / StarTech.com](https://www.startech.com/en-us/cables/usb-30) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Solution (Pick-n-Place) – UFACTORY Official Website](https://www.ufactory.cc/solution-pickandplace/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Product Page (xArm) – UFACTORY Official Website](https://www.ufactory.cc/xarm-collaborative-robot/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [UFACTORY USA](https://www.ufactory.us/product/ufactory-xarm-camera-stand) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Robot Dog Go2_Quadruped_Robot Dog Company / Unitree Robotics](https://www.unitree.com/go2/) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [Unitree Go2 Servo Robotic Arm D1](https://www.usrobotstore.com/products/unitree-go2-servo-robotic-arm-d1) | 200 | Expected page title returned; no access restriction identified by the automated check. |
| [www.westerndigital.com](https://www.westerndigital.com/products/hdd/internal-hdd) | 200 | Confirmed the internal-HDD catalog in the browser. |

The owner replaced the Vention invitation URL with the direct MachineBuilder link for design 506323. That replacement was checked in the browser and also redirects to sign-up when signed out. The Vention HTTP status in the table describes the earlier invitation-link check; the direct replacement was verified by browser navigation.
