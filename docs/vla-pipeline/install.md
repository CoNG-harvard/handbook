# Install the arm software

**Run on the shared Linux workstation.** Finish [computer preparation](../getting-started/computer.md) first. These steps install software; they do not launch arm movement.

## 1. Put the lab source files in place

Obtain the [arm setup handoff](../getting-started/sources.md#arm-platform-files) and unpack it into your home folder. Preserve this structure:

```text
~/lerobot/
  lerobot/                         modified LeRobot source
  lerobot_robot_xarm/               arm plugin
  lerobot_camera_imageclient/       camera plugin
  lerobot_teleoperator_xr/           headset plugin
  xr_teleoperate/teleop/teleimager/  camera server
  xr_teleoperate/teleop/televuer/    headset web interface
  scripts/                         launcher, reset, and rig configurations
~/robocoop/
  run_xarm_inference.py
  run_xarm_inference.yaml
  models/download_model.py
  openpi/                          lab model-server source, including uv.lock
```

The upstream LeRobot repository alone does not contain the lab's changes to recording and recovery. Use the supplied version and its accompanying dependency snapshot.

```bash
ls ~/lerobot/scripts/run_teleop.sh
ls ~/lerobot/lerobot_robot_xarm/pyproject.toml
ls ~/robocoop/run_xarm_inference.yaml
```

**Expected:** all three paths are printed without `No such file`.

## 2. Create the recording environment

The installed lab environment uses Python **3.10**. TeleImager's inspected package specifically requires Python older than 3.11. Do not put the openpi server in this environment.

```bash
conda create -n lerobot python=3.10 -y
conda activate lerobot
python --version
```

**Expected:** Python 3.10.x.

Use the maintainer's exported package constraints if supplied. The commands below follow the inspected package manifests, but have not been tested together on an empty workstation. If pip reports incompatible requirements, save the error and use the maintainer's known-working dependency set; do not remove version constraints at random.

```bash
cd ~/lerobot
python -m pip install -e ./lerobot \
  -e './xr_teleoperate/teleop/teleimager[server]' \
  -e ./xr_teleoperate/teleop/televuer \
  -e ./lerobot_robot_xarm \
  -e ./lerobot_camera_imageclient \
  -e ./lerobot_teleoperator_xr \
  'xarm-python-sdk==1.17.3' 'pyrealsense2==2.56.5.9235' \
  'numpy<2' scipy pyyaml
```

`-e` means the package uses the source folder directly, so keep these folders in place. Avoid the old blanket `xr_teleoperate/requirements.txt` recipe: its older package pins differ from the inspected LeRobot installation.

```bash
python -m pip check
python -c "import lerobot, lerobot_robot_xarm, lerobot_camera_imageclient, lerobot_teleoperator_xr; print('Arm plugins found')"
command -v lerobot-record
command -v teleimager-server
```

**Expected:** no broken requirements, `Arm plugins found`, and paths to both programs. If the active environment is wrong, run `conda activate lerobot` and check again.

## 3. Give the camera software access to USB devices

For the RealSense driver and device-access rules, use the [official Linux installation instructions](https://github.com/realsenseai/librealsense/blob/master/doc/distribution_linux.md) for your Ubuntu version. Installing the Python package alone may not grant USB access. The bundled TeleImager also provides `setup_uvc.sh` for video-device access; have the administrator review and run it when needed.

With the cameras connected and no other camera program running:

```bash
conda activate lerobot
teleimager-server --cf --rs
```

**Expected:** the connected cameras and their serial numbers are listed. Match each serial to its physical camera and record it. If a camera is missing, check the USB data cable, port, device permissions, and whether another application is using it.

## 4. Connect the headset

Enable developer mode for your Quest account/headset through Meta's current developer setup flow. Download **Android SDK Platform Tools for Linux** from the [official Platform Tools page](https://developer.android.com/tools/releases/platform-tools). Extract the `platform-tools` folder to `~/lerobot/platform-tools`.

Connect the headset over USB, put it on, and accept the USB debugging prompt for your workstation. Then run:

```bash
~/lerobot/platform-tools/adb devices
```

**Expected:** one line per headset, with its serial and the word `device`. `unauthorized` means you still need to approve the prompt in the headset. A charging-only cable may produce no device at all. See [Android's connection instructions](https://developer.android.com/tools/adb).

## 5. Create the local HTTPS certificate

The headset web page uses HTTPS, so it needs a certificate. On this new workstation, create one for the local connection:

```bash
mkdir -p ~/.config/xr_teleoperate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ~/.config/xr_teleoperate/key.pem \
  -out ~/.config/xr_teleoperate/cert.pem \
  -subj '/CN=localhost' \
  -addext 'subjectAltName=DNS:localhost,IP:127.0.0.1'
chmod 600 ~/.config/xr_teleoperate/key.pem
```

The inspected TeleVuer and TeleImager packages can read this folder. Keep `key.pem` private. If a browser later shows a certificate warning, check that it is your expected local service. Connections using a workstation IP need a certificate valid for that address and may need separate browser trust setup.

## 6. Adapt the launcher to your account

Open the script in an editor:

```bash
nano ~/lerobot/scripts/run_teleop.sh
```

Near the top, replace the original account-specific paths with:

```bash
ADB_PATH="$HOME/lerobot/platform-tools"
DATASETS_DIR="$HOME/lerobot/datasets"
```

In nano, press **Ctrl+O**, then **Enter** to save; **Ctrl+X** exits. Keep the workspace at `~/lerobot` because the launcher also changes into that folder.

**Installation checkpoint:** plugins import, both command-line tools exist, cameras are discovered, and `adb devices` reports your headset. You are ready to [configure the station](teleop/setup.md). Model-server installation is covered separately in [Run a trained model](inference/index.md).
