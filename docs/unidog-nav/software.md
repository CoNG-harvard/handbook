---
hide:
  - footer
---

# Self Improvement Learning basic software

**Goal:** check the Go2's manufacturer interface, onboard-computer access, and both cameras. Finish [equipment and connections](hardware.md) and [D1 mounting](d1-arm.md) first. Have the operator handle power-on and keep the platform stationary during these checks.

## 1. Connect with Unitree's tools

Install the app from [Unitree's Go2 download page](https://www.unitree.com/app/go2/) on the operator's phone. Follow the supplied Go2 instructions to pair with the intended robot and confirm its identity and connection status. Have the supplier identify the D1 control interface supported by the delivered arm and firmware; check its connection separately from the dog.

**Expected:** the operator can identify and connect to the Go2 and D1. Demonstrating movement and stop controls belongs in the supervised readiness check.

## 2. Check onboard-computer access

Keep the delivered operating system and device configuration. Ask the owner for the onboard computer's address, your authorized login, and the network connection to use. Confirm that SSH access is enabled on that computer.

On the workstation, `ssh -V` should show an OpenSSH version. If the command is missing, install [Ubuntu's OpenSSH client](https://ubuntu.com/server/docs/how-to/security/openssh-server/):

```bash
sudo apt update
sudo apt install openssh-client
```

Connect from the workstation, replacing both placeholders, including the angle brackets:

```bash
ssh <ROBOT_USER>@<ONBOARD_COMPUTER_IP>
```

Check a new host's fingerprint with the owner before accepting it. **Expected:** a terminal on the onboard computer. Run `exit` to return to the workstation. A login confirms computer access, not readiness of the robot's control system.

If the connection times out, check the address and network with the owner. `Permission denied` means the login or key needs checking; it does not call for reinstalling the robot's software.

## 3. Check the front and wrist cameras

Use the [shared camera check](../getting-started/software.md#3-install-realsense-viewer) on the computer each camera is physically connected to. The front camera is a **D435i**; the D1 wrist camera is a **D435**. Confirm the wrist camera's USB host before installing tools there.

Have the installer show Viewer on that host's display or its approved remote desktop. An ordinary SSH terminal does not display the graphical Viewer.

**Expected:** two live views with the correct serials and positions. Preserve the installed camera configuration and calibration when checking them.

**Next:** [Hardware readiness](readiness.md).
