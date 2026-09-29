# Basic software scope and source checks — 2026-09-28

The owner expanded the handbook from hardware-only setup to include basic software, while excluding the lab's research. Added workstation/GPU/camera preparation and one device-connection page per platform. The research installation pages remain archived and outside the site build and search index.

## Sources checked

- [Ubuntu Desktop installation](https://ubuntu.com/tutorials/install-ubuntu-desktop): operating-system preparation and Terminal access.
- [Ubuntu NVIDIA drivers](https://ubuntu.com/server/docs/how-to/graphics/install-nvidia-drivers/) and [NVIDIA kernel modules](https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/kernel-modules.html): driver guidance. No fixed driver version or CUDA toolkit recipe added.
- [RealSense Linux packages](https://github.com/realsenseai/librealsense/blob/master/doc/distribution_linux.md): Viewer, utilities, device rules, and kernel compatibility. The package page advertises multiple Ubuntu releases but lists narrower DKMS kernel support; therefore the handbook requires matching the kernel instead of claiming a universal Ubuntu 24.04 recipe.
- [RealSense Jetson installation](https://github.com/realsenseai/librealsense/blob/master/doc/installation_jetson.md): separate onboard-computer installation route.
- [UFACTORY browser connection](https://help.ufactory.cc/en/articles/4204606-guide-to-control-ufactory-xarm-by-tablet): control-box address and port 18333. The handbook uses placeholders and wired station networking.
- [Meta device setup](https://developers.meta.com/horizon/documentation/native/android/mobile-device-setup/), [Android Platform Tools](https://developer.android.com/tools/releases/platform-tools), and [ADB](https://developer.android.com/tools/adb): developer mode, USB authorization, and device enumeration.
- [Unitree Go2 app](https://www.unitree.com/app/go2/): official download and supplied manuals. No assumed D1-specific interface, default credentials, firmware update, or control command added.
- [I2RT software setup](https://doc.i2rt.com/getting-started/sw-setup), [I2RT source](https://github.com/i2rt-robotics/i2rt), and [YAM Cell](https://doc.i2rt.com/products/yam-cell): SDK environment, import check, CAN discovery and persistent names. The upstream SDK recommends Ubuntu 22.04/Python 3.11; that is identified separately from the lab's Ubuntu 24.04 workstation. The four-CAN powered-leader example is not assumed to match an unconfirmed ABC Box variant.

## Limits and validation

SSH attempts to both original remote desktops timed out. Archived setup pages were reviewed for context, but their lab environments, bridges, model servers, and research launchers were not restored or claimed to be reverified.

Documentation checks cover the MkDocs strict build, all generated local links and anchors, and browser layout/navigation. They do not establish a tested fresh installation, successful device communication, or hardware acceptance. No packages were installed on the workstation or robot computers and no robot commands were run.

## Follow-up review

Reviewed all four software pages and their setup/readiness links at the owner's request. Corrections:

- Separated workstation tool preparation from camera tests after physical assembly; removed premature camera-streaming requirements from workstation preparation.
- Check existing NVIDIA/RealSense installations first. Added explicit RealSense utilities and USB rules, without prescribing DKMS for every kernel. Retained distinct Jetson guidance.
- Added the D405 matching resolution/frame-rate requirement from [RealSense support](https://github.com/realsenseai/librealsense/discussions/11689); require noting tested settings rather than implying arbitrary USB streaming capacity.
- Added Ubuntu USB rules, group membership, and a fresh login for Quest, following [Android's device setup](https://developer.android.com/studio/run/device). Kept headset enumeration distinct from working teleoperation.
- Made the I2RT SDK path conditional on the delivered configuration, added explicit environment activation, and limited the import result to package discovery. No pip command is assumed inside a uv-created environment.
- Added SSH client prerequisites and network/login troubleshooting; kept the Go2 system image unchanged.
- Removed firmware updates from normal connection checks and distinguished factory/current xArm addresses.
- Removed the headset-video acceptance statement that depended on an application outside this basic setup.

All 16 distinct external URLs in the final four software pages returned HTTP 200 with normal certificate verification. The old `help.ufactory.cc` link failed hostname verification and was replaced with the current [Studio connection guide](https://docs.ufactory.cc/user_manual/ufactoryStudio/3.connection.html) and [Studio introduction](https://docs.ufactory.cc/user_manual/ufactoryStudio/1.preface.html), both verified. HTTP success confirms availability, not all hardware claims.

The final review also checked the strict site build, local links/anchors on all 22 pages, shell syntax for the software snippets after placeholder substitution, and desktop/mobile rendering. Hardware and fresh-install validation remain outstanding; the remote repository access limit noted above still applies.
