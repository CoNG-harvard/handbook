# First supervised dog movement

**Goal:** perform one short, intentional movement and end the session. Complete the [live camera check](robot-bridge.md) first. An experienced operator must be beside the robot with access to its physical stop control.

## 1. Agree on the test

Use a clear, measured area with enough space for standing, turning, and stopping. Confirm the selected robot, camera, battery readiness, and stop procedure. Run only one controller: no simultaneous voice listener, benchmark, or autonomous loop.

For the first trial, ask the operator to choose one supported short command, such as a 15-degree turn. The first motion request can also make the dog **stand up** as part of its readiness sequence.

## 2. Run the read-only preflight

**On the shared workstation:**

```bash
cd "<NAV_DIR>"
bash scripts/prepare_real_robot.sh --check
```

Read the entire output. The inspected script checks the expected robot branch/files and reports workstation service status without starting or restarting services. It can print `CHECK OK` while reporting a model or segmentation service as down; this message does not establish that all services or hardware are ready.

If it reports modified tracked files or the wrong branch on the robot, ask the owner to reconcile the deployment. Do not discard changes or change branches to bypass the check.

## 3. Start a foreground bridge for this navigation test

A direct-command test does not need Qwen or segmentation. Use the bridge in a visible terminal so the operator can see its logs and close it at the end. This still requires the commissioned robot and the successful code preflight above.

The owner must first stop the existing camera-check bridge, if it is still running. To identify it, run on the workstation:

```bash
ssh unitree 'pgrep -af "[p]rimitive_server.py"'
```

Have the owner stop the identified server through its service manager or its specific process ID. Do not start a second server on the same port or stop an unrelated process.

In **Terminal A**, open a robot login and start the bridge there:

```bash
ssh unitree
```

After the robot login prompt appears, run **on the robot**:

```bash
python3 "<ROBOT_TOOLS_DIR>/primitive_server.py" --real --per-call \
  --skills-repo "<ROBOT_SKILLS_DIR>" --walk-python "<ROBOT_PYTHON>"
```

This command runs **on the robot**. It enables real execution; keep Terminal A open. The path arguments must match your [bridge setup](robot-bridge.md); use the camera settings approved there. Use the owner's reviewed arguments if those differ.

In **Terminal B**, on the workstation:

```bash
cd "<NAV_DIR>"
bash scripts/robot_tunnel.sh up
python3 scripts/robot_client.py health
```

**Expected:** `"ok": true`, `"real": true`, and `"busy": false`. A port error or startup traceback is a failed setup, not permission to continue.

The alternative all-services launcher, `bash scripts/prepare_real_robot.sh`, starts Qwen and segmentation as well as the bridge. Use that only for the complete deployment described in the [handoff inventory](../getting-started/sources.md#dog-platform-files); it is not needed for this direct navigation test.

## 4. Send one command

Prepare **Terminal C** on the workstation with the same repository open so the software abort command is ready:

```bash
cd "<NAV_DIR>"
```

During a session, the abort command is:

```bash
python3 scripts/robot_client.py stop
```

It depends on a working tunnel and executor; the operator's physical stop remains necessary.

In **Terminal B**, with the operator's agreement:

```bash
cd "<NAV_DIR>"
python3 scripts/robot_client.py start-episode
python3 scripts/robot_client.py exec "The next action is turn left 15 degrees."
```

`start-episode` resets episode bookkeeping; the following motion plan can trigger standing and readiness checks. **Expected:** the dog completes the agreed movement, stops, and the client reports results. If the physical behavior or the returned result is unexpected, stop and investigate before sending another command.

A command succeeding once does not validate autonomous navigation. Continue to benchmark/model workflows only with their operator procedures.

## 5. End the session

1. Send `python3 scripts/robot_client.py stop` while the tunnel is still connected.
2. Confirm with the operator that movement has stopped and use the agreed physical resting/shutdown procedure.
3. With the robot stopped, press Ctrl+C in Terminal A to end the foreground bridge, then type `exit` to leave the robot login. Closing the tunnel alone does not disable a background server.
4. Close your tunnel with `bash scripts/robot_tunnel.sh down`.
5. Stop model services you started only after confirming nobody else is using them.

For problems, retain the foreground bridge output from Terminal A and the client output. Background helper launches write their robot log at `<ROBOT_LOG_DIR>/primitive_server.log`; this foreground launch prints to Terminal A instead. Describe the requested command and observed motion to the platform owner.
