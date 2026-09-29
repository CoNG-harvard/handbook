---
hide:
  - footer
---

# VLA Pipeline basic software

**Goal:** see both xArm control boxes, all five cameras, and the connected Quest headsets from the workstation. Finish [equipment and connections](hardware/index.md) and [shared software setup](../getting-started/software.md) first. Keep motion disabled during these connection checks.

Before powering the equipment, complete the [pre-power inspection](readiness.md#1-inspect-before-power-on) with the installer.

## 1. Open each arm in UFACTORY Studio

UFACTORY Studio is the manufacturer's graphical control interface. Use a browser on the workstation; the control box serves the interface.

1. Obtain the current address of each control box and match it to **rig A** or **rig B**. The box label gives its factory address; use the owner's record if it has changed.
2. Have the installer put the workstation and control boxes on the same network range, with a different address for every device. If the boxes share a factory address, configure them one at a time.
3. Open `http://<CONTROL_BOX_IP>:18333`, replacing the placeholder with that box's address.
4. Repeat for the second box. Record the displayed device identity, firmware version, and any reported errors.

**Expected:** each address opens the intended arm's Studio interface. Leave enabling, jogging, and resets to the supervised readiness check. Firmware updates are a separate maintenance task, not a connection test. See [UFACTORY's browser connection instructions](https://docs.ufactory.cc/user_manual/ufactoryStudio/3.connection.html) and [Studio documentation](https://docs.ufactory.cc/user_manual/ufactoryStudio/1.preface.html).

## 2. Identify the five cameras

Follow the [RealSense Viewer check](../getting-started/software.md#4-check-each-camera). Record **rig A wrist — D405**, **rig B wrist — D405**, and the positions of the **three D415 scene cameras**. Confirm all five views are available together.

## 3. Check Quest USB connections

For a wired developer connection, follow [Meta's device setup](https://developers.meta.com/horizon/documentation/native/android/mobile-device-setup/). The headset's account needs verified developer access and developer-team membership before enabling developer mode.

On the Ubuntu workstation, install Android's USB permission rules:

```bash
sudo apt update
sudo apt install android-sdk-platform-tools-common
id -nG
```

If `plugdev` is missing from the group list, run the following as your normal login user, then **log out and log back in**:

```bash
sudo usermod -aG plugdev "$USER"
```

These steps follow [Android's Ubuntu USB setup](https://developer.android.com/studio/run/device). Download [SDK Platform Tools for Linux](https://developer.android.com/tools/releases/platform-tools), extract the archive, and open its `platform-tools` folder in Terminal. Android Studio is not needed for this connection check.

Connect a headset with its USB data cable. Put it on and approve USB debugging for this workstation, then run:

```bash
./adb devices -l
```

**Expected:** a serial followed by `device` for each attached headset. `unauthorized` means the headset has not approved the connection; `no permissions` points to the Ubuntu USB setup above. If no device appears, check the data cable and developer mode. Label each headset's rig assignment; this check establishes USB access, not a teleoperation session.

**Next:** [Hardware readiness](readiness.md).
