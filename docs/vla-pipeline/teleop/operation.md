# Record your first demonstration

**Goal:** save one short episode and find its folder. Complete [Configure and start](setup.md) first. Keep a second person beside the arm, watching the movement area and stop control.

## 1. Check the view

In the Quest browser, open `https://localhost:8012/?ws=wss://localhost:8012` and enter VR while looking forward. Confirm the camera images are live and correctly assigned. Before an episode begins, moving your hand should not start a recording.

## 2. Learn the controls

<figure class="handbook-figure" markdown="1">

![Quest controllers with the main buttons labeled.](../assets/quest_controllers.png)

<figcaption markdown="1">

Quest controller buttons used during recording. The table below explains each control.

[View full-size image](../assets/quest_controllers.png)
{ .figure-links }

</figcaption>

</figure>

| Control | What happens |
|---|---|
| Right **B** | Starts an episode; press again to finish it |
| Right **grip/side button** | Closes the gripper while held; release to open |
| Right **trigger**, after ending | Saves the episode |
| Left **trigger**, after ending | Discards the episode |
| Right **A**, while waiting or at a recovery prompt | Resets the arm to home; this moves it |

When you press B, the program connects your current hand position to the arm's current position. The arm then follows your **relative** hand movement. Start with a small, slow movement. In the lab implementation, holding the trigger during teleoperation can increase movement scaling; leave it released for your first trial.

The gripper's orientation behavior depends on `record.teleop.fix_ee_angle`. It is not guaranteed to stay pointing down unless the selected configuration enables that behavior.

## 3. Save one short episode

1. With the operator's agreement, use **A** while waiting if the arm needs to return home.
2. Hold your controller still, then press **B**.
3. Make one small movement in a clear area. For the first trial, prioritize checking control rather than finishing a pick-and-place task.
4. Press **B** again to end the episode.
5. Use the **right trigger** at the confirmation prompt to save it.
6. Read the terminal/headset confirmation before starting another episode.

If you choose the left trigger, that episode is discarded. Previously saved episodes remain.

## 4. Find the saved recording

Use the dataset path printed when the launcher started. New sessions created by the inspected launcher go under `<RECORDING_DIR>/datasets/test_a_<timestamp>/`; older sessions may be under `<RECORDING_DIR>/xr_teleoperate/datasets/`.

After ending the session normally, inspect the folder:

```bash
ls "<DATASET_FOLDER>"
ls "<DATASET_FOLDER>/meta"
```

Replace `<DATASET_FOLDER>` with the actual path. **Expected:** dataset metadata and recorded data, with video files according to the configured format. A directory existing by itself does not prove an episode was saved; check the recording confirmation and dataset metadata too.

## 5. End the session

1. End/save or discard the current episode.
2. Put the arm in the agreed resting pose while the area is clear.
3. Press **Ctrl+C** in the recording terminal and allow it to finish writing files.
4. The camera server may remain in the `teleop_imgserver` tmux session. If you started it and nobody else needs it, stop it with `tmux kill-session -t teleop_imgserver`.
5. Follow the manufacturer's shutdown procedure for the arm. Disconnect the headset only after the session has ended.

## If something goes wrong

For unexpected movement, use the physical stop control. For a normal end, use the application controls above.

A collision or controller error can leave the arm unable to accept commands. Stop, inspect the cause with the operator, and follow the controller's recovery instructions. The modified recording program may display “Restart the arm, then press A to continue.” Only press A after the operator confirms the workspace and controller are ready: recovery can move the arm home.

The lab's recovery flow discards an interrupted partial episode and keeps previously saved episodes. Repeatedly pressing reset will not fix a mechanical obstruction or a fault that requires a power cycle.

**Next:** [Prepare recordings](datasets.md), or [test a trained model](../inference/index.md).
