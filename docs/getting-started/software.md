---
hide:
  - footer
---

# Basic software

**Goal:** prepare the shared workstation to recognize the GPU, connect to equipment, and display camera images. Complete [workstation preparation](computer.md) first. Each project's **Basic software** page then covers its device tools.

**Using TurtleBot3?** Go to its [basic software guide](../turtlebot3/software.md). Its ROS environment is separate from these GPU and RealSense checks.

Do steps 1–3 on the workstation first. Return to the camera check in step 4 after your platform's equipment is connected. Keep any working supplier installation; install only the tools that are missing.

## 1. Prepare Ubuntu

The reference workstation runs **Ubuntu 24.04 on an x86-64 PC**. For a new computer, have the installer follow the [Ubuntu Desktop installation guide](https://ubuntu.com/tutorials/install-ubuntu-desktop). Back up existing files before installing an operating system.

Keep the Go2's onboard computer and the ABC Box PC on their supplier-supported images. [I2RT currently recommends Ubuntu 22.04](https://doc.i2rt.com/getting-started/sw-setup) for its SDK; confirm the chosen host with the supplier before changing the shared workstation's operating system.

Open **Terminal** with **Ctrl+Alt+T**. Run each line separately:

```bash
lsb_release -ds
uname -m
uname -r
```

**Expected:** the installed Ubuntu version, `x86_64`, and a kernel version. The kernel is the part of Linux that manages hardware; save its version when asking for driver help.

## 2. Check the NVIDIA driver

A driver lets Ubuntu communicate with the graphics card. First check the existing installation:

```bash
nvidia-smi
```

**Expected:** a table identifying the **RTX PRO 6000 Blackwell Workstation Edition** and driver version. If it appears, keep the working driver.

If the command fails or the GPU is absent, have the installer use [Ubuntu's driver installation instructions](https://ubuntu.com/server/docs/how-to/graphics/install-nvidia-drivers/). Blackwell requires NVIDIA's [open kernel modules](https://download.nvidia.com/XFree86/Linux-x86_64/610.43.02/README/kernel_open.html); choose a supported driver for this GPU rather than copying an older example version. Restart after installation and run the check again.

A CUDA toolkit or machine-learning environment is not needed for these device checks.

## 3. Install RealSense Viewer

RealSense Viewer displays camera images without a robot application. On the computer receiving the camera's USB cable:

1. If Viewer already opens and detects the cameras, keep that installation.
2. Otherwise, follow the official [RealSense Linux package instructions](https://github.com/realsenseai/librealsense/blob/master/doc/distribution_linux.md) to add its signing key and package source. Then install the utilities and USB permission rules:

```bash
sudo apt update
sudo apt install librealsense2-utils librealsense2-udev-rules
```

`sudo` requests your workstation password; no characters appear while you type it.

Have the installer check kernel compatibility before adding `librealsense2-dkms`. The [source-install guide](https://github.com/realsenseai/librealsense/blob/master/doc/installation.md) also describes when kernel patches are needed. Use one installation method; do not mix package and source installations to fix a missing camera.

Reconnect the camera and open Viewer from a terminal on its host's desktop:

```bash
realsense-viewer
```

For the Go2's onboard computer, use the supplier's installed tools or the [RealSense Jetson guide](https://github.com/realsenseai/librealsense/blob/master/doc/installation_jetson.md); the workstation's driver recipe is not interchangeable with it.

## 4. Check each camera

With the robot stationary:

1. Close other camera applications, select one camera in Viewer, and note its model and serial.
2. Start its color and depth streams with settings supported by that camera. For the D405, use matching resolution and frame rate for both streams, following [RealSense's guidance](https://github.com/realsenseai/librealsense/discussions/11689).
3. Match the image to the physical camera. Repeat for each camera, then show the required views together on their connected hosts.
4. Record resolution and frame rate along with each serial. Check for frozen images or repeated disconnects. A pass applies to the tested settings, not every possible streaming rate.
5. Close Viewer before another application opens the cameras.

| Platform | Views to identify |
|---|---|
| VLA Pipeline | 2 D405 wrists and 3 D435 scene views |
| Self Improvement Learning | D435i front and D435 wrist, on their connected hosts |
| ABC Box | 3 D405 views: left wrist, right wrist, and overhead |

**Ready when:** the workstation recognizes its GPU and, after assembly, each connected camera produces a stable, correctly identified image.

**Next:** follow your platform's setup sequence: [VLA Pipeline](../vla-pipeline/index.md#set-up-the-platform) · [Self Improvement Learning](../unidog-nav/index.md#set-up-the-platform) · [ABC Box](../abc-box/index.md#set-up-the-platform) · [TurtleBot3](../turtlebot3/index.md#set-up-the-platform).
