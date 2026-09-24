# Configure and start the arm station

**Run on the arm workstation.** Complete [installation](../install.md) and [hardware setup](../hardware/index.md) first. The station has two arms; validate rig A first, then repeat the checks for rig B.

## 1. Fill in the rig configuration

```bash
nano ~/lerobot/scripts/configs/rig_a.yaml
```

This file has two main sections: **`rig`** identifies the headset/cameras, and **`record`** contains the recording settings. Edit the supplied complete file. The abbreviated example below shows the structure; it is **not a replacement for the whole file**.

```yaml
rig:
  quest_serial: "<QUEST_SERIAL>"
  cameras:
    wrist_camera: "<WRIST_CAMERA_SERIAL>"
    right_3pv_camera: "<SCENE_CAMERA_SERIAL>"
record:
  robot:
    type: xarm_robot
    xarm_ip: "<ARM_IP>"
  teleop:
    type: xr_teleoperator
    xarm_ip: "<ARM_IP>"
    img_server_ip: "<CAMERA_WORKSTATION_IP>"
    vuer_port: 8012
  dataset:
    push_to_hub: false
```

Use the same arm address in both places. Keep `push_to_hub: false` to save recordings locally.

| Setting in the full file | What to check |
|---|---|
| `rig.quest_serial` | Matches the headset listed by `adb devices` |
| `rig.cameras` | Each topic points to the correct camera serial |
| `record.robot.cameras` | Includes only cameras you intend to record; each `camera_name` matches a topic |
| Camera `host` | `localhost` if the camera server runs on this workstation |
| `record.teleop.img_server_ip` | Address of the camera workstation reachable by this setup |
| `record.teleop.wrist_camera_name` / `right_3pv_camera_name` | Match the corresponding camera topics |
| `record.teleop.fix_ee_angle` | Ask the operator whether to use `ground` to keep the gripper pointing down; the inspected rig A file leaves this setting commented out |

Extra topics such as `cube_cam2` or `3pv_3` belong to the lab's expanded station. Remove unused camera entries from your rig and recording configuration rather than retaining serials for devices you do not have.

The launcher reads **all** `scripts/configs/*.yaml` files when synchronizing camera serials. Move unused rig manifests outside that folder on a one-rig installation, or update their camera identities consistently. Two manifests must not assign different serials to the same camera topic.

## 2. Check the camera server settings

Open:

```bash
nano ~/lerobot/xr_teleoperate/teleop/teleimager/cam_config_server.yaml
```

Keep the supplied full configuration and update the relevant camera sections. Each enabled camera needs the correct serial and supported image settings. For cameras you do not have, disable both `enable_zmq` and `enable_webrtc`, and remove references to them in the recording configuration.

The launcher synchronizes serial numbers from `rig.cameras` into **existing** topics in this file. It does not create new camera sections or remove unused ones. Check that the wrist image really comes from the wrist camera.

## 3. Test the cameras before moving the arm

In **Terminal A**:

```bash
conda activate lerobot
teleimager-server --rs
```

On the workstation, open the preview addresses configured in `cam_config_server.yaml`. For the reference rig these are:

- Wrist view: `https://localhost:60001/`
- Scene view: `https://localhost:60004/`

**Expected:** live images from the correct cameras. Put a hand in front of each camera to identify it. A page loading without an image is not a successful camera check.

After checking, press **Ctrl+C** in Terminal A to stop this test server. The launcher will start its own shared camera server. If the preview reports a certificate or USB error, resolve it using [installation](../install.md) before continuing.

## 4. Review the first reset with an operator

!!! warning "The next command moves the arm"
    `run_teleop.sh` resets the arm to its home position and opens the gripper **before** you start a recording. Have the operator confirm the home pose in `scripts/reset_xarm_home.py`, the selected arm address, the clear workspace, and the physical stop control.

Do not run an inference client or a second teleoperation session for the same arm.

## 5. Start one recording session

In **Terminal A**:

```bash
cd ~/lerobot
conda activate lerobot
bash scripts/run_teleop.sh a "Pick a red cube and put it in the basket"
```

The launcher starts/reuses the camera server, connects the headset to the web page over USB, resets the arm, and starts recording software. It prints the rig, task, and dataset folder. Keep this terminal open.

**Expected:** rig A is selected, the reset completes, and a dataset path similar to `~/lerobot/datasets/test_a_<timestamp>` appears. Note the **actual printed path** for later.

On the Quest, open its browser and enter:

```text
https://localhost:8012/?ws=wss://localhost:8012
```

The launcher makes this address work through USB using `adb reverse`. Use this headset address even when a second rig uses a different workstation port. Enter VR while looking forward.

**Expected:** the wrist/scene views appear and the application waits for you to start an episode. Continue to [Record your first demonstration](operation.md).

## If setup stops

| What you see | What to do |
|---|---|
| `conda: command not found` | Reopen Terminal or source Conda as shown in [computer preparation](../../getting-started/computer.md) |
| Camera topic missing / serial conflict | Check both configuration files and all rig manifests; confirm each enabled camera is connected |
| Headset `unauthorized` | Put on the headset and approve USB debugging |
| Vuer port already in use | An earlier session may still be running. Close your previous session; do not start a competing controller |
| Camera server failed | Read its log with `tmux attach -t teleop_imgserver`; detach with **Ctrl+B**, then **D** |
| Headset page does not open | Check the USB cable, `adb devices`, certificates, and the launch terminal's first error |
| Arm reset fails | Keep the arm stopped and have the operator inspect the controller error and physical setup |

## Validate rig B and choose two-arm control

After rig A works, configure `rig_b.yaml` for the second installed arm, with its own headset, cameras, and workstation Vuer port. Repeat the camera, home-pose, and recording checks for rig B. The launcher's two-headset mode maps each headset's local port 8012 to its configured workstation port.

```bash
cd ~/lerobot
bash scripts/run_teleop.sh b "Your task description"
```

Two-arm control from one headset uses `bimanual.yaml`:

```bash
cd ~/lerobot
BIMANUAL=1 bash scripts/run_teleop.sh "Your task description"
```

**This resets and enables both arms.** The operator must review both home poses and the shared workspace first. Do not use two-arm mode as the first installation test.
