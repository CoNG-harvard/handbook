# Source files, handoff, and verification

This page is for the person preparing the installation files and for readers who need to understand the limits of this manual. **Review date: 24 September 2026.**

The setup steps were checked against source on the two lab workstations. The Self Improvement Learning mock bridge was also run locally with a stored test image: health returned `ok: true`, `backend: mock`, and `real: false`, and the client retrieved an identical JPEG. No hardware commands were run. Public upstream projects provide part of the software; they do not fully reproduce the lab's working folders.

## Arm platform files

The arm inference folder, represented here by `<INFERENCE_DIR>`, is a workspace, not a top-level Git repository. Its inference code uses `--config` and a YAML settings file. The associated recording workspace is `<RECORDING_DIR>/`.

Provide a dated source bundle containing:

| Folder/file | Why the new installation needs it |
|---|---|
| `<RECORDING_DIR>/lerobot/` | Modified LeRobot source, including local recording and dataset changes |
| `<RECORDING_DIR>/lerobot_robot_xarm/` | xArm driver plugin |
| `<RECORDING_DIR>/lerobot_camera_imageclient/` | Image-server camera plugin |
| `<RECORDING_DIR>/lerobot_teleoperator_xr/` | Quest control plugin |
| `<RECORDING_DIR>/xr_teleoperate/teleop/teleimager/` and `televuer/` | Modified camera and headset packages, including camera configuration |
| `<RECORDING_DIR>/scripts/` | Launcher, rig manifests, reset routine, and dataset preparation tools |
| `<INFERENCE_DIR>/run_xarm_inference.py` and `.yaml` | Inference client and complete settings |
| `<INFERENCE_DIR>/models/download_model.py` | Checkpoint downloader |
| `<INFERENCE_DIR>/openpi/`, with lockfile and submodules | Lab model-server fork and client package |
| One processed dataset + matching checkpoint | A first prediction check with known input |

The inspected openpi fork is [edgeyyzhang/openpi](https://github.com/edgeyyzhang/openpi), at commit `b7a2912` before accounting for any local changes. Its upstream is [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi). Record the exact commit **and local modifications** in the bundle; a commit identifier alone is not a working-tree snapshot.

Do not ship another person's passwords, SSH keys, Hugging Face tokens, or HTTPS private keys. Provide sanitized configuration templates and communicate new device identities privately. Generate fresh HTTPS keys on the new workstation.

### A practical source transfer

If the new workstation has authorized access to the reference machine, the maintainer can use `rsync` to copy selected directories into a **new, empty** local workspace. Replace `<ARM_SOURCE_HOST>` with the source host alias and `<SOURCE_RECORDING_DIR>` with the absolute recording-workspace path on that source host. `<RECORDING_DIR>` is your new local destination; the two paths need not match. Run on the **new workstation**:

```bash
mkdir -p "<RECORDING_DIR>"
rsync -av --exclude='.git' --exclude='.venv' --exclude='__pycache__' \
  --exclude='datasets' --exclude='logs' --exclude='.env*' \
  --exclude='*.pem' --exclude='.claude' \
  '<ARM_SOURCE_HOST>:<SOURCE_RECORDING_DIR>/lerobot' \
  '<ARM_SOURCE_HOST>:<SOURCE_RECORDING_DIR>/lerobot_robot_xarm' \
  '<ARM_SOURCE_HOST>:<SOURCE_RECORDING_DIR>/lerobot_camera_imageclient' \
  '<ARM_SOURCE_HOST>:<SOURCE_RECORDING_DIR>/lerobot_teleoperator_xr' \
  '<ARM_SOURCE_HOST>:<SOURCE_RECORDING_DIR>/xr_teleoperate' \
  '<ARM_SOURCE_HOST>:<SOURCE_RECORDING_DIR>/scripts' "<RECORDING_DIR>/"
```

This preserves source changes but deliberately does not migrate installed environments or dataset collections. The exclusions are a starting point, not a substitute for reviewing the bundle. Transfer the listed VLA Pipeline source files, the complete approved openpi source/lockfile, and the chosen model/sample dataset separately. Check for symlinks pointing outside the copied folders.

### Record the working dependency set

On the reference arm workstation, these commands **print** the environment information for a maintainer to save and review:

```bash
conda env export -n lerobot --no-builds
conda run -n lerobot python -m pip freeze --exclude-editable
conda run -n lerobot python -m pip list --editable
```

Exported files can contain absolute paths and private package URLs. Replace/remove machine-specific paths and reattach the supplied source packages at their new locations. Do not present an unreviewed export as a portable lockfile.

The observed runtime uses Python 3.10.20, LeRobot 0.4.4, Torch 2.7.1, TeleImager 1.5.0, TeleVuer 4.0.0, xArm SDK 1.17.3, and pyrealsense2 2.56.5.9235. These are reference versions, not proof that independently resolving those packages reproduces every dependency.

## Dog platform files

The active workstation checkout is `<NAV_DIR>`, with origin [CoNG-harvard/unidog_nav](https://github.com/CoNG-harvard/unidog_nav), at commit `edee63b` plus local changes at review time. An older nested checkout exists inside `LLM_guided_RL`; do not use it as the current workstation source by accident.

| Required item | Handoff detail |
|---|---|
| Main source + NaVILA submodule | Commit IDs and a reviewed snapshot of intended local changes |
| Sample JPEGs | Include `test_frames/real_front_wall1` or another agreed image folder |
| Qwen environment, if using Qwen | Python 3.12 package snapshot and CUDA/driver requirements; the launcher assumes a pip-installed CUDA 13 layout |
| NaVILA environment and checkpoint, if using NaVILA | Setup script, model files, and any local submodule changes |
| Robot-side `LLM_guided_RL` | Correct deployment revision, expected branch, SDK and hardware dependencies |
| Robot `walk` environment | Architecture-appropriate environment and confirmed `run_skill.py` operation |
| Bridge files | `primitive_server.py`, `run_plan.py`, and `grab_realsense_frame.py` |
| Robot configuration | Interface, camera, stop procedure, and applicable calibrations |

The all-services helper `scripts/prepare_real_robot.sh` additionally needs the following locations. The maintainer must update its deployment-specific paths to match them:

- Workstation `<WORKSTATION_SKILLS_DIR>/scripts/serve_segmentation.py` and its dependencies.
- Workstation `<SEGMENTATION_ENV_DIR>/bin/python`, model assets, and a working segmentation service on port 8090.
- A clean robot-side skills checkout on `offline-rl-vlm-policy`.

Its `--check` mode reports service availability but can still finish successfully when those services are down. Its real startup path starts services and replaces the robot bridge. Use it only with that full deployment installed.

The bridge's default camera is now RealSense; older README paragraphs describe the built-in Go2 camera. The robot-side companion README also describes a newer uv environment while this bridge still defaults to the deployed Python 3.8 `walk` environment. A maintainer must resolve that deployment difference before commissioning a new robot image.

## Self Improvement Learning platform photograph

The supplied [platform PDF](../unidog-nav/assets/platform.pdf) shows the Self Improvement Learning setup and labels its Unitree Go2, Unitree D1 arm, and D435i camera. The website displays a rendered copy with those labels preserved. The photograph does not establish the exact Go2 edition, onboard computer model, internal wiring, or software readiness.

## RTX PRO 6000 hardware standard

The planned setup uses **one shared workstation with one RTX PRO 6000 Blackwell Workstation Edition, 96 GB**, serving both projects. The source-machine inventory confirms that card in the arm workstation; the inspected source code still comes from two separate remote installations. No remote hardware or environment was changed by this documentation update.

The workstation and platform hardware lists distinguish observed equipment, software-described robot parts, and the selected new-machine configuration. CPU/RAM/storage were inspected with `lscpu`, `free`, and `lsblk`; GPU identities with `nvidia-smi`; connected cameras with `lsusb`. The robot onboard computer's exact Jetson model and custom mounts still need a physical/vendor inventory.

Before a fresh RTX PRO 6000 installation is signed off, validate the Qwen and openpi environments on Blackwell and provide a compatible NaVILA environment. The inspected legacy NaVILA Torch 2.3/CUDA 12.1 setup predates that support and is retained only as provenance, not as the new workstation installation recipe.

## What was verified for this handbook?

| Evidence | What it establishes |
|---|---|
| Arm `scripts/run_teleop.sh` and rig manifests | `rig`/`record` nesting, serial synchronization, home reset, USB forwarding, dataset folder |
| Arm package manifests and installed package metadata | Source package locations, Python constraints, observed versions |
| `run_xarm_inference.py` and `.yaml` | YAML-only settings, mode dispatch, live connection timing, saved-data mode avoiding robot connection |
| openpi `serve_policy.py`, `pyproject.toml`, README | Server arguments and separate environment workflow |
| Dog `robot_tunnel.sh`, `prepare_real_robot.sh`, `robot_client.py`, `primitive_server.py` | Tunnel behavior, real-mode reuse, camera default, dependencies, supported CLI |
| Dog `agent_ai/start_vllm.sh`, NaVILA setup script, package metadata | Model startup assumptions and environment separation |

## Remaining validation for a release

The handbook build can check page structure and links. It cannot verify USB permissions, GPU compatibility, headset certificate behavior, robot calibration, or successful movement.

Before calling this a fully validated installation release, a maintainer should install the supplied bundle on a fresh workstation, resolve and save dependency locks, run both no-motion checks, and record a supervised hardware acceptance test. The missing robot-image/environment release and lab-specific source distribution are explicit handoff requirements, not steps a beginner is expected to guess.

## Follow-up source check

On **24 September 2026**, the handbook was checked again against the original remote working trees. The arm openpi checkout remains at `b7a2912`; the active `unidog_nav` checkout remains at `edee63b` with local changes. The companion `LLM_guided_RL` workstation checkout reports `459bceb`; this does not establish the revision deployed on the robot.

- **Arm setup:** `scripts/run_teleop.sh` confirms separate rig A/B manifests, the shared camera server, USB forwarding, and resets before recording. The TeleImager manifest requires Python below 3.11; the arm plugin requires at least 3.10. The current inference script accepts `--config`, and its `from_dataset` handler avoids robot connection. The older `<INFERENCE_DIR>/setup.md` still shows superseded CLI flags, so the handbook follows executable source.
- **Arm hardware:** USB enumeration again reported two D405 and three D415 cameras. The source contains rig A, rig B, and bimanual configurations. Enumeration and configuration files do not replace a physical inventory of mounts, cables, and controllers.
- **Dog setup:** the bridge source confirms a fully local `--mock` mode, the RealSense default for the robot deployment, and the separate `--real` execution flag. The tunnel helper can reuse a running server without changing its mode.
- **Models:** installed package metadata reports vLLM 0.24.0, Torch 2.11.0+cu130, Transformers 5.13.0, CUDA nvcc 13.2.78, and CUDA runtime 13.0.96. The Qwen launcher uses Python 3.12 CUDA paths and port 8000. The legacy NaVILA installer still selects a CUDA 12/Torch 2.3 FlashAttention wheel. These observations do not validate either model on a fresh RTX PRO 6000 installation; see [optional model setup](../unidog-nav/models.md).
- **D1:** the companion D1 interface and `unidog_nav/robot/arm_reach.py` establish the SDK, robot deployment, and camera-to-arm calibration dependencies. They do not supply a complete tested installation handoff. The [D1 readiness page](../unidog-nav/d1-arm.md) records the outstanding items.

**Executed check:** copies of the original `primitive_server.py`, `primitive_specs_snapshot.json`, `robot_client.py`, and one supplied JPEG were used for a local mock test on port 18766. Health returned `ok: true`, `backend: mock`, `real: false`, and `busy: false`; the retrieved JPEG matched the input byte-for-byte. The test server was then stopped. No robot commands or model servers were started, and the remote working trees were not modified.
