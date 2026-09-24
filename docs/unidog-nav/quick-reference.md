# Dog quick reference

Use this page **after** completing [workstation setup](setup.md) and [robot connection](robot-bridge.md). All commands below run on the workstation in `<NAV_DIR>`. Replace paths using your [folder choices](../getting-started/paths.md).

## Read status or view the camera

```bash
cd "<NAV_DIR>"
bash scripts/robot_tunnel.sh status
python3 scripts/robot_client.py health
python3 scripts/robot_client.py image "<LIVE_IMAGE_PATH>"
ssh unitree 'tail -50 "<ROBOT_LOG_DIR>/primitive_server.log"'
```

Health: `ok` means the bridge answered; `real` tells you whether physical actions are enabled; `busy` means a plan is running. Check the actual values.

## Open a connection without requesting real mode

```bash
cd "<NAV_DIR>"
bash scripts/robot_tunnel.sh up --start-server
python3 scripts/robot_client.py health
```

This reuses an existing server if present, even if it is already in real mode. Inspect health before issuing any action.

## Prepare a supervised real session

```bash
cd "<NAV_DIR>"
bash scripts/prepare_real_robot.sh --check
```

Follow [First supervised movement](first-run.md) for the real-mode startup, dependencies, and operator checks. The preflight alone does not enable real mode or prove the whole platform ready.

## Request a software stop

```bash
cd "<NAV_DIR>"
python3 scripts/robot_client.py stop
```

For unexpected physical motion, use the robot's physical stop procedure. The command above requires the bridge connection to work.

## Close your tunnel

```bash
cd "<NAV_DIR>"
bash scripts/robot_tunnel.sh down
```

This does not stop the robot or shut down its server. Follow the [session shutdown steps](first-run.md#5-end-the-session).

## Check a Qwen model server

```bash
curl --fail http://127.0.0.1:8000/v1/models
```

For installation and startup, see [model setup](models.md#choose-a-model). Coordinate GPU use before switching between Qwen and NaVILA.
