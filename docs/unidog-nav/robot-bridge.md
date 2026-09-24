# Connect the workstation to the dog

**Goal:** retrieve a live camera image without issuing a movement command. Finish the [mock bridge check](setup.md#2-run-a-mock-bridge-with-no-robot) first.

## 1. Prepare the robot computer with the platform owner

The robot's onboard computer must already have the hardware-specific operating system/drivers and the correct robot-control software. Do not install the workstation's x86-64 Conda or CUDA packages on a Jetson/ARM computer.

The inspected workstation scripts expect:

| On the robot | Requirement |
|---|---|
| `<ROBOT_SKILLS_DIR>/` | Approved robot-control checkout; preflight expects branch `offline-rl-vlm-policy` |
| `scripts/run_skill.py` inside that checkout | Entry point for supported robot skills |
| Hardware Python environment | Full path `<ROBOT_PYTHON>` to the approved environment's Python executable, with the robot SDK |
| `<ROBOT_TOOLS_DIR>/` | Bridge program and its helper files |
| Camera | Default in the current bridge is a USB RealSense D435i; built-in front camera is an explicit alternative |
| Network interface | Reference scripts use `eth0`; this is a device name, not an IP address |

Have the owner supply the commissioned robot image/environment and verify stop handling. **A complete fresh robot-image installation is not yet reproducible from the two workstation repositories alone.** The [handoff page](../getting-started/sources.md) lists the missing release artifacts. You can complete workstation and mock setup while this hardware preparation is arranged.

## 2. Configure the SSH connection — on the workstation

Obtain the robot's address and login account. Edit `~/.ssh/config` (create the directory/file if needed) and add:

```sshconfig
Host unitree
    HostName <DOG_IP>
    User <ROBOT_USER>
```

`unitree` is the alias the workstation scripts use. It need not match the robot's actual hostname. Your laptop's aliases are not automatically present on the new workstation.

```bash
ssh unitree 'hostname'
```

On first connection, confirm the host fingerprint with the owner. **Expected:** the robot computer's name. Configure your authorized SSH key with the owner, then check the noninteractive login used by the tunnel helper:

```bash
ssh -o BatchMode=yes unitree 'hostname'
```

If this fails, resolve login/key access before proceeding.

## 3. Install the matching bridge files

**On the workstation, with the owner's approved robot checkout in place:**

```bash
cd "<NAV_DIR>"
ssh unitree 'mkdir -p "<ROBOT_TOOLS_DIR>"'
scp robot/primitive_server.py robot/run_plan.py \
  robot/grab_realsense_frame.py "unitree:<ROBOT_TOOLS_DIR>/"
```

Do this for a new installation or a coordinated update, not while another operator is running the robot. The bridge uses the companion skills repository; copying these files alone does not install that repository or its SDK.

Before running the helper scripts, have the owner update their robot-side tools, log, skills, and Python paths to your chosen locations. In particular, `robot_tunnel.sh` must start the bridge from `<ROBOT_TOOLS_DIR>`, write its log under `<ROBOT_LOG_DIR>`, and pass your `--skills-repo` and `--walk-python` values. The service and voice launchers must use the same choices; replacing paths in this manual does not change their built-in defaults. `primitive_server.py --help` documents `--skills-repo`, `--walk-python`, `--iface`, and `--camera`.

## 4. Start the bridge without real motion

**On the workstation:**

```bash
cd "<NAV_DIR>"
bash scripts/robot_tunnel.sh status
bash scripts/robot_tunnel.sh up --start-server
python3 scripts/robot_client.py health
```

The helper opens an SSH tunnel: requests to workstation port **8766** reach the robot's bridge. If no server is running, `--start-server` starts the default server with a real camera and pretend skills.

!!! important "Check the actual mode"
    The helper can reuse an existing server, including one already running in real mode. It does not turn real mode off. For this setup check, expect `"ok": true`, `"real": false`, and `"busy": false`. If `real` is true or the server is busy, coordinate with its operator before changing anything. Health and image requests themselves do not issue movement.

## 5. Capture and inspect a live image

```bash
cd "<NAV_DIR>"
python3 scripts/robot_client.py image "<LIVE_IMAGE_PATH>"
```

Open `<LIVE_IMAGE_PATH>` in the workstation's image viewer. **Expected:** the current view from the selected robot camera. Change something visible in the scene and capture again to confirm it is fresh.

A healthy bridge does not guarantee that its camera works. The current default is RealSense; older notes describing the built-in camera refer to `--camera front`. Ask the owner to select the intended camera rather than swapping blindly between feeds.

## If the connection fails

| Symptom | Check |
|---|---|
| SSH hostname cannot be resolved | `Host unitree` exists in this workstation's SSH configuration |
| SSH timeout | Robot power, network connection, and robot address |
| `Permission denied` | Login account and authorized SSH key |
| Local port 8766 occupied | Use `robot_tunnel.sh status`; do not kill an unknown process |
| Server fails to start | Read `ssh unitree 'tail -50 "<ROBOT_LOG_DIR>/primitive_server.log"'` |
| Image request fails | Camera selection, USB access, helper file, and robot Python dependencies |
| `real: true` during a no-motion check | An existing real-mode server is running; coordinate with the owner |

## Finish the camera-only session

```bash
cd "<NAV_DIR>"
bash scripts/robot_tunnel.sh down
```

This closes the workstation tunnel. **It leaves the robot server running and does not stop motion.** If the owner wants the default background server shut down, they should stop that specific service/process after confirming no client needs it.

**Next:** [First supervised movement](first-run.md).
