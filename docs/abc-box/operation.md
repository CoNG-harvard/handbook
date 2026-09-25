# Configure and record

**Goal:** save one short, supervised demonstration. Complete the [software rehearsal](install.md) first. A trained operator must be present for calibration and the first real session.

## 1. Match the configuration to the equipment

On the recording computer:

```bash
cd "<ABC_DIR>"
source .venv/bin/activate
nano configs/station_yam.yaml
```

Edit the supplied complete file. Confirm the follower model, gripper, and each leader-to-follower pairing. Set `save_root` to your full `<ABC_DATA_DIR>` path. Persistent robot/controller changes belong in this YAML file; the web interface's temporary changes do not replace it.

The inspected passive-GELLO configuration uses these CAN names:

| Device | Interface |
|---|---|
| Left follower | `can_left` |
| Right follower | `can_right` |
| Left leader | `can_lead_l` |
| Right leader | `can_lead_r` |

Have the installer follow [I2RT's hardware setup](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md) to assign persistent names, configure CAN permissions, and calibrate the leaders. Its permission helper changes sudo rules; the administrator should review and apply it as part of station setup. Do not substitute the different bus names from a YAM Cell example.

Leader zeroing writes calibration to the encoders. The operator must check the required pose and released trigger before using **Zero L / Zero R**. Follow the procedure for the actual leader type.

## 2. Identify the cameras

```bash
yam-abc-cameras
nano configs/cameras.yaml
```

Replace every example serial with your own device's serial. Map `top`, `left`, and `right` to the overhead, left-wrist, and right-wrist views agreed for this station. Keep those role names consistent with the recording/model configuration.

```bash
yam-abc-doctor
```

**Expected:** the intended CAN devices and cameras are found. Resolve failures before proceeding. Missing optional policy backends are not a reason to install training software for collection. [Configuration source](https://github.com/i2rt-robotics/yam-abc-reproduce/tree/main/configs)

## 3. Preview before enabling motion

```bash
yam-abc-gui --host 127.0.0.1
```

Open `http://127.0.0.1:8042` on this computer. The camera views open before **Start Teleop** touches the robots. Identify each view by moving an object in front of its camera. Confirm all three are live and correctly assigned.

!!! warning "Start Teleop can move the arms"
    Starting real teleoperation builds the hardware drivers, may calibrate grippers by driving them to their limits, and moves followers toward the leaders' pose. Clear the jaws and workspace, align the leaders as instructed, and have the operator ready at the physical stop before clicking it.

## 4. Record one short episode

1. Set a clear **Task** name and confirm the real recording output folder.
2. With the operator's agreement, click **Start Teleop**. Check a small, slow movement before attempting a task.
3. Click **Start Recording**, make one controlled movement, then click it again to finish.
4. Wait for saving to finish. In **Review**, refresh and play the episode; check each camera view and the recorded arm-action traces.

**Expected:** one completed episode under `<ABC_DATA_DIR>/<task-slug>/<episode-id>/`. A task slug is the task name converted into a folder-friendly label. A folder alone does not prove the recording is complete.

The top handle button toggles synchronization; the second toggles recording in the documented workflow. Confirm those controls on your supplied leader. [I2RT Collect & Review](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/collect.md)

## 5. End the session

Finish and save the recording, then have the operator guide the arms to the approved resting arrangement. Use **End Session** and follow the supplier's physical shutdown procedure. Close the application with Ctrl+C when finished and back up the episode.

For unexpected movement, use the physical stop. The application's **E-STOP** keeps motor power on to hold position and discards a recording still in progress. **Power Off Arms** and **Reset Session** can remove torque, so support the arms first. Software controls do not replace the physical stop. [Control behavior](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/collect.md#bottom-tray)

**After the first session:** see the [reference and model handoff](reference.md). Training is not required to complete teleoperation setup.
