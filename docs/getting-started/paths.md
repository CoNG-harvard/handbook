# Choose your folders

The manual uses placeholders for installation folders. Choose locations on your own computer and record them in your private setup note. You do not need to reproduce the lab desktops' directory layout.

## How to replace a placeholder

Before copying a command, replace the entire placeholder, including `<` and `>`, with a **full absolute path**. Keep the quotation marks. Use the same replacement throughout the guide.

For example, `cd "<NAV_DIR>"` means “open the folder where you installed the navigation project.” These placeholders are text to replace, not shell variables. Use `pwd` inside a folder to see its full path; do not put `~` inside quoted paths or YAML settings.

Choose simple folder names without spaces or quotation marks for compatibility with the supplied helper scripts. Keep the source's internal filenames and subfolders unchanged.

## On the shared workstation

| Placeholder | Your chosen location |
|---|---|
| `<RECORDING_DIR>` | Arm recording workspace containing `scripts/`, `lerobot/`, and the custom plugins |
| `<INFERENCE_DIR>` | Arm inference workspace containing `run_xarm_inference.py` and `openpi/` |
| `<NAV_DIR>` | Main `unidog_nav` checkout |
| `<CONDA_DIR>` | Conda installation folder |
| `<WORKSTATION_SKILLS_DIR>` | Workstation copy of `LLM_guided_RL`, for workflows that need its perception services |
| `<SEGMENTATION_ENV_DIR>` | Segmentation service's Python environment, when required |

The Qwen launcher expects `agent_ai/.venv` **inside** `<NAV_DIR>`; the openpi environment belongs inside `<INFERENCE_DIR>/openpi`. Those internal locations are software conventions, not references to a particular desktop.

## On the robot's onboard computer

| Placeholder | Your chosen location |
|---|---|
| `<ROBOT_SKILLS_DIR>` | Approved `LLM_guided_RL` robot checkout |
| `<ROBOT_TOOLS_DIR>` | Folder containing the bridge and helper files |
| `<ROBOT_PYTHON>` | Full path to the approved hardware environment's Python executable |
| `<ROBOT_LOG_DIR>` | Folder used for the background bridge log |
| `<HAND_EYE_FILE>` | Approved camera-to-arm calibration JSON file |

Robot paths refer to the robot's filesystem even when written inside an SSH or file-transfer command on the workstation. They can differ from workstation paths.

## Images and source transfers

`<MOCK_IMAGE_PATH>` and `<LIVE_IMAGE_PATH>` are full output filenames ending in `.jpg` on the workstation. Choose an existing writable parent folder. `<TEST_IMAGES_DIR>` is the supplied sample JPEG folder. Dataset, checkpoint, and other input-image placeholders elsewhere in the guide refer to the files supplied for that test.

For source transfers, `<ARM_SOURCE_HOST>` is the source computer's SSH alias and `<SOURCE_RECORDING_DIR>` is its recording workspace. These identify the copy source; `<RECORDING_DIR>` identifies your separate destination.

## Match the launchers to these locations

Some original scripts contain fixed deployment paths. The maintainer must adapt the supplied copy before the first hardware session:

- **Arm recording:** update `ADB_PATH`, `DATASETS_DIR`, and the workspace `cd` in `scripts/run_teleop.sh`, as shown in [arm installation](../vla-pipeline/install.md#6-adapt-the-launcher-to-your-account).
- **Dog bridge:** update tools/log paths and pass `--skills-repo` and `--walk-python` consistently in the tunnel, preflight, service, and voice helpers. See [bridge preparation](../unidog-nav/robot-bridge.md#3-install-the-matching-bridge-files).
- **Model and perception helpers:** update the Conda activation path in the evaluation wrapper and the workstation skills/segmentation paths in the service launcher. Review model paths and other absolute paths in the handed-off configuration too.

Changing directory in a terminal does not override a path written inside a script. Complete the mock and camera checks after adapting the deployment.

Standard locations such as `~/.ssh/config`, the camera packages' `~/.config/xr_teleoperate` certificate folder, and temporary installer files under `/tmp` retain their normal meanings on the current computer.

**Next:** [Prepare the shared computer](computer.md).
