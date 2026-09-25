# Install and rehearse

**Run on the ABC recording computer.** For a factory-configured Box, first ask the supplier which software is installed and preserve its configuration. Use the fresh-install steps below only for the agreed I2RT collection stack.

## 1. Get the software handoff

Obtain the supported Linux image, leader/gripper types, camera identities, calibration procedure, and approved source revision. Choose an empty `<ABC_DIR>` and an `<ABC_DATA_DIR>` for recordings. Both are full paths on this computer; see [Choose your folders](../getting-started/paths.md).

The selected source uses Python 3.12 and uv. Install uv using the [shared tool instructions](../getting-started/computer.md#4-install-uv); the RTX driver and other projects' environments are not prerequisites for this recording path.

## 2. Install the collection application

```bash
sudo apt update
sudo apt install -y git build-essential python3-dev

git clone https://github.com/i2rt-robotics/yam-abc-reproduce.git "<ABC_DIR>"
cd "<ABC_DIR>"
git checkout "<ABC_SOURCE_REVISION>"
```

Use the revision supplied for your station. The [reference page](reference.md) records the revision inspected for this guide.

The repository's I2RT submodule uses SSH by default. For a public HTTPS download, configure this checkout's submodule URL before downloading it:

```bash
git submodule init
git config submodule.third_party/i2rt.url https://github.com/i2rt-robotics/i2rt.git
git submodule update --init --recursive
uv sync --frozen --extra camera --extra gui
```

This installs the collection and review tools into `<ABC_DIR>/.venv`. No policy backend is needed. Keep the same extras when syncing again, because uv removes packages outside the requested environment. These steps follow the [I2RT installation guide](https://github.com/i2rt-robotics/yam-abc-reproduce#install).

```bash
source .venv/bin/activate
command -v yam-abc-gui
```

**Expected:** the command resolves inside this project's `.venv`. Keep build errors for the maintainer; do not resolve them by changing another project's environment.

## 3. Rehearse without hardware

```bash
cd "<ABC_DIR>"
source .venv/bin/activate
yam-abc-gui --mock --host 127.0.0.1
```

On the **same computer**, open `http://127.0.0.1:8042`. The source's `--mock` option selects simulated robots and cameras. This confirms the application flow, not device readiness. [GUI command source](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/yam_abc_reproduce/cli.py)

1. In **Collect**, set a task name such as `software rehearsal`.
2. Set the output folder to a dedicated mock subfolder within `<ABC_DATA_DIR>`.
3. Click **Start Teleop**, then **Start Recording**.
4. Stop recording after a few seconds.
5. Open **Review**, refresh the list, and play the episode.

**Expected:** an episode appears with simulated views. Keep these recordings separate from real demonstrations. End the mock session and press **Ctrl+C** in its terminal before opening a real session.

**Next:** [Configure and record](operation.md).
