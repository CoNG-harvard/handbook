---
hide:
  - footer
---

# TurtleBot3 basic software

**Goal:** connect the operator computer to one robot and check sensor data without commanding motion. Complete [equipment and connections](hardware.md) first.

Before powering the equipment, complete the [pre-power inspection](readiness.md#1-inspect-before-power-on) with the installer.

## 1. Choose the matching environment

The documented lab installation uses **Ubuntu 20.04 and ROS 2 Foxy** on the robots. Confirm this on the actual unit before installing anything on the operator computer.

| Situation | What to do |
|---|---|
| Using an existing lab robot | Preserve its working image. Use the owner's matching operator environment and installed device configuration |
| Preparing a new operator computer for a Foxy robot | Have the installer provide an Ubuntu 20.04/Foxy environment with working robot-network access. Follow the [official Foxy installation guide](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html) only inside that environment |
| Building a new robot installation | Select a currently supported combination from [ROBOTIS PC setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/) and its linked SBC and OpenCR setup instructions. Configure the computer, robot image, packages, and firmware together |

Foxy's support ended in May 2023 ([ROS support schedule](https://www.ros.org/reps/rep-2000.html#foxy-fitzroy-may-2020-may-2023)). It is documented here for the existing robots, not as the default for a new build. Do not install Foxy packages directly on the shared **Ubuntu 24.04** system or substitute Humble instructions for a Foxy robot.

These basic checks need neither the workstation GPU nor RealSense Viewer. Confirm the operator environment with the owner before buying another computer or changing the shared workstation.

## 2. Check access and versions

On the **operator computer**, open Terminal. Check that `ssh -V` shows an OpenSSH version; if it is missing on Ubuntu, install the client with `sudo apt update` followed by `sudo apt install openssh-client` ([Ubuntu instructions](https://ubuntu.com/server/docs/how-to/security/openssh-server/)). Replace both placeholders, including the angle brackets, with the login and address supplied privately by the owner:

```bash
ssh <ROBOT_USER>@<ROBOT_IP>
```

On first connection, verify the host identity with the owner before accepting it. A successful login opens a terminal on the robot. There, run:

```bash
lsb_release -ds
ls /opt/ros
```

**Expected for the documented installation:** Ubuntu 20.04 and a `foxy` directory. These show the OS and installed ROS directories, not which environment a running process uses. If they differ, use instructions for the installed version.

Run `exit` to return to the operator computer. Check the same two commands there. In a confirmed Foxy environment, load ROS in each terminal used for ROS commands:

```bash
source /opt/ros/foxy/setup.bash
printenv ROS_DISTRO
```

**Expected:** `foxy`. For another ROS release, use its own setup instructions and matching environment on both ends.

## 3. Check robot discovery and sensors

Have the installer check the [ROBOTIS network and bringup requirements](https://emanual.robotis.com/docs/en/platform/turtlebot3/bringup/): both ends need the agreed ROS domain (discovery group) and compatible communication settings, and the network must allow discovery traffic. Being on the same Wi-Fi alone is not sufficient.

Start with **one robot** and no active motion controller. The owner starts the installed device services; for an unmodified kit, follow the matching ROS version of ROBOTIS bringup. Preserve existing lab robot configuration.

On the operator computer, in the configured ROS terminal:

```bash
ros2 node list
ros2 topic list
```

**Expected:** the intended robot's nodes and sensor topics, including laser scans and odometry (wheel-based position estimates). Names may include a robot-specific prefix. Have the installer show live scans and changing timestamps in the matching ROS visualization tool; a listed topic alone does not prove that readings are arriving.

For multiple robots, confirm each robot's identity and command routing before enabling motion. Do not assume the standard vendor launch creates the lab's robot names or namespaces.

## 4. Optional: check OptiTrack

On the **Motive computer**, have the tracking-system operator create or select a [rigid body](https://docs.optitrack.com/motive/rigid-body-tracking) for the robot's markers, with a unique name, and confirm stable live tracking.

For the documented VRPN route, enable the rigid-body stream in [Motive's streaming settings](https://docs.optitrack.com/motive/data-streaming). The receiving computer must use the same rigid-body name and the correct server address.

The existing arrangement uses a ROS 1 client and a ROS 1-to-ROS 2 bridge. Use the maintained installation supplied by the owner; the bridge and its host must be identified before this optional step. VRPN itself is not restricted to ROS 1. Confirm fresh position readings in ROS and the correct robot identity, rather than merely checking that a topic exists. Have the tracking operator verify that the coordinate axes and ground-plane origin match the receiving ROS environment; a live stream can still use the wrong reference frame.

**Ready when:** the intended robot's live sensor readings are visible, software versions match, and optional tracking works if needed.

**Next:** [Hardware readiness](readiness.md).
