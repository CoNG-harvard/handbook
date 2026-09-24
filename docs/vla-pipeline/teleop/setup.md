# Setup

## Python environment (TODO: more specific, code)
install xr_teleop, then install lerobot. Finally, pip install -e all packages

```bash
cd ~/lerobot/xr_teleoperate
conda activate lerobot
```

## Prerequisites

- The hardware is correctly assembled - see [Hardware](../hardware/index.md#assembly-and-networking).
- three identities : the **arm IPs**, the **Quest serials**, and the **camera serials**.


## Configuration (one-time, after assembly)

The three identities from assembly go into two YAML files (plus one line in the
launch script for the Quest serial).

### 1. Record config (`scripts/configs/*.yaml`)

`lerobot-record` reads all robot/teleop/dataset parameters from a per-rig YAML config,
loaded with `--config_path`:

| Config | Used for |
|---|---|
| `scripts/configs/rig_a.yaml` | rig A — single arm, wrist + scene cameras |
| `scripts/configs/rig_b.yaml` | rig B — single arm, wrist camera only |
| `scripts/configs/bimanual.yaml` | one headset driving both arms |

Set the arm IP, Vuer port, image-server IP, and camera topics here (`rig_a.yaml`
shown):

```yaml
robot:
  type: xarm_robot
  xarm_ip: <ARM_A_IP>            # static IP set on the arm's control box (step 1)
  record_xr_debug: true
  cameras:
    wrist_camera:
      type: imageclient
      host: localhost
      request_port: 60000
      camera_name: wrist_camera     # must match a key in cam_config_server.yaml (step 3)
      width: 640
      height: 480
      fps: 30
    right_3pv_camera:
      type: imageclient
      host: localhost
      request_port: 60000
      camera_name: right_3pv_camera
      width: 640
      height: 480
      fps: 30

teleop:
  type: xr_teleoperator
  xarm_ip: <ARM_A_IP>
  img_server_ip: <WORKSTATION_IP>       # workstation running teleimager-server
  vuer_port: 8012                   # one per headset; matches the adb reverse mapping (step 2)
  wrist_camera_name: wrist_camera
  right_3pv_camera_name: right_3pv_camera
  input_mode: controller
  display_mode: immersive-wrist
  vr_position_smoothing_alpha: 0.7  # feel/behaviour knobs — fine to leave as-is
  fix_ee_angle: ground
  xr_pose_fps: 60

dataset:
  repo_id: my_user/xarm_xr_dataset_run_a
  push_to_hub: false
  fps: 30

display_data: false
```

The per-session values — `dataset.root` (a unique timestamped folder) and
`dataset.single_task` — are deliberately **not** in the file: `run_teleop.sh` generates
the dataset folder and passes both on the CLI (see [Quick start](#quick-start-script)).
The bimanual config uses `type: bimanual_xarm` / `bimanual_xr` with
`right_xarm_ip` / `left_xarm_ip` and `right_cameras` / `left_cameras`.

### 2. Camera serials → topics (`cam_config_server.yaml`)

The `camera_name` values above are just labels; the image server maps each one to a
physical camera by **serial number** in
`xr_teleoperate/teleop/teleimager/cam_config_server.yaml`. Paste in the serials you
recorded in assembly step 3:

```yaml
wrist_camera:                       # arm A wrist D405
  type: realsense
  serial_number: "<WRIST_CAM_A_SERIAL>"
right_3pv_camera:                   # arm A scene D415
  serial_number: "<SCENE_CAM_A_SERIAL>"
wrist_camera_b:                     # arm B wrist D405
  serial_number: "<WRIST_CAM_B_SERIAL>"
```

### 3. Quest serial (`scripts/run_teleop.sh`)

The headset serial isn't a recording parameter, so it's the one identity that stays in
the launch script. Set it in the per-rig `case` block (find it with
`platform-tools/adb devices`):

```bash
case "$RIG" in
  a) QUEST_SERIAL="<QUEST_A_SERIAL>" ;;
  b) QUEST_SERIAL="<QUEST_B_SERIAL>" ;;
esac
```

The arm IP and Vuer port the script needs (to reset the arm and set up `adb reverse`)
are read straight from the rig's YAML, so they can't drift from what `lerobot-record`
uses.

| Parameter | Recorded in | Where to set it |
|---|---|---|
| Arm IP(s) | Assembly step 1 (static address) | `scripts/configs/rig_*.yaml` (`xarm_ip`, or `right_xarm_ip` / `left_xarm_ip`) |
| Vuer port | one per headset | `scripts/configs/rig_*.yaml` (`vuer_port`) |
| Image-server IP | workstation address | `scripts/configs/rig_*.yaml` (`img_server_ip`) |
| Camera topics | — | `scripts/configs/rig_*.yaml` (`camera_name`, `*_camera_name`) |
| Camera serials → topics | Assembly step 3 (serial number) | `cam_config_server.yaml` |
| Quest serial | Assembly step 2 (`adb devices`) | `scripts/run_teleop.sh` `case` block (`QUEST_SERIAL`) |

## Quick start (script)

```bash
cd ~/lerobot
./scripts/run_teleop.sh                              # rig a, default task
./scripts/run_teleop.sh "task description"           # rig a, custom task
./scripts/run_teleop.sh b "task description"         # rig b (second arm + headset)
BIMANUAL=1 ./scripts/run_teleop.sh "task description"  # one headset, both arms
```

The script:

1. Activates the `lerobot` conda env and picks the rig config (`scripts/configs/rig_<rig>.yaml`, or `bimanual.yaml` when `BIMANUAL=1`).
2. Starts the camera image server (`teleimager-server`) in a tmux session `teleop_imgserver` — skipped if one is already running. View its logs with `tmux a -t teleop_imgserver` (detach with ++ctrl+b++ then ++d++).
3. Sets up the `adb reverse` tunnel (port 8012) so the headset can reach the teleop page on `localhost`.
4. Resets the xArm to its home position with the gripper open.
5. Launches `lerobot-record --config_path=<rig config>`, auto-generating a unique dataset folder under `datasets/test_<rig>_<timestamp>/` (or `datasets/bimanual_<timestamp>/`).

## Manual steps

If you're not using the script, run these in order.

**1. Camera image server**

```bash
teleimager-server --rs
```
The server should be visible at `https://localhost:60001/` and `https://localhost:60004/`.

**2. adb reverse tunnel** (first time the Quest is connected)

```bash
export ADB_PATH=~/lerobot/platform-tools/platform-tools   # adjust to your platform-tools path
if [ -z "$($ADB_PATH/adb -s <QUEST_SERIAL> reverse --list)" ]; then
    $ADB_PATH/adb -s <QUEST_SERIAL> reverse tcp:8012 tcp:8012
fi
```

**3. Reset the arm to home** (gripper open) before/after a session

```bash
python scripts/reset_xarm_home.py --ip <ARM_IP>
# optional: --speed 10   (joint move speed in deg/s)
```

**4. Launch recording**

Point `lerobot-record` at the rig config and pass the per-session dataset values:

```bash
lerobot-record \
    --config_path=scripts/configs/rig_a.yaml \
    --dataset.root=~/lerobot/datasets/test_a_$(date +%Y%m%d_%H%M%S) \
    --dataset.single_task="Pick a red cube and put it in the basket"
```

Any field in the config can be overridden on the CLI (CLI wins), e.g.
`--display_data=true` or `--teleop.fix_ee_angle=null`.

Then open the teleop page on the headset — see [Operation](operation.md).

## Useful options

These live in the rig config (`scripts/configs/*.yaml`); set them there, or override on
the CLI for a one-off run (CLI wins):

- **`fix_ee_angle: ground`** (`--teleop.fix_ee_angle=ground`) — locks the end-effector vertical (gripper points straight down; yaw still follows your wrist twist) and disables the thumbstick orientation lock/unlock. Set to `null` for full 6-DOF orientation control.
- **`single_task`** (`--dataset.single_task="…"`) — the natural-language task label stored with the episodes; `run_teleop.sh` passes this from its task argument.
- **`display_data: true`** (`--display_data=true`) — opens a live data view on the workstation (useful for debugging; adds overhead).
- **`push_to_hub: true`** (`--dataset.push_to_hub=true`) — push the dataset to the Hugging Face Hub (off by default).

### Appending to an existing dataset (e.g. a new task)

Pass the existing dataset directory as the third argument to `run_teleop.sh`, with a new
task:

```bash
./scripts/run_teleop.sh a "Pick a green cube and put it in the basket" \
    ~/lerobot/datasets/test_a_<existing_timestamp>
```

Or, launching manually, point `--dataset.root` at it:

```bash
lerobot-record \
    --config_path=scripts/configs/rig_a.yaml \
    --dataset.root=~/lerobot/datasets/test_a_<existing_timestamp> \
    --dataset.single_task="Pick a green cube and put it in the basket"
```
