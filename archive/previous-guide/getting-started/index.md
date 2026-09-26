# Before you begin

**Goal:** know what you are setting up and have the information needed to finish. Read this page once before installing anything.

## 1. Choose a project

**VLA Pipeline** is a tabletop setup with two xArm 7 robots. A person can guide it using a Meta Quest headset and controllers. The computer can save the camera images and movements as a demonstration. Later, a trained model can choose movements itself. The hardware list covers **both arms**. Validate rig A first, repeat for rig B, then configure the intended two-arm workflow.

**Self Improvement Learning** uses a Unitree Go2 robot dog with a Unitree D1 arm. A workstation looks at camera images and sends commands to a separate computer carried by the dog. The dog also needs the lab's robot-control software. Installing the workstation software alone does not make an unconfigured dog ready to walk.

**ABC Box** is a separate two-arm station controlled through hand-operated leader arms. Start with its [hardware and software guide](../abc-box/index.md). Its included recording computer handles the first collection session; shared GPU preparation is needed only for later model work.

Use the [hardware checklist](hardware.md) to gather the full station, including the **RTX PRO 6000 Blackwell Workstation Edition, 96 GB**, in one workstation shared by both projects.

## 2. Get a setup handoff from the lab

Get these items **before starting the project installation**. Ask the project owner to check each item with you and save the details in a private setup note.

### For both projects

- [ ] A named lab contact who can provide files and help with the first session.
- [ ] Access to the shared workstation, permission to install software, and access to the required code.
- [ ] The [project equipment](hardware.md), network details, and an operator for the first hardware check.

### Before installing VLA Pipeline

- [ ] A dated bundle of the modified `lerobot` workspace, `robocoop` scripts, and lab `openpi` source, including its lockfile.
- [ ] The recording environment's dependency snapshot and instructions for recreating it. A fresh installation is still pending validation.
- [ ] Separate rig A/B settings: arm addresses, camera/headset serials, and reviewed home positions.

A model checkpoint and matching sample dataset are needed only for **Run a trained model**, not for the first headset recording. There is no verified public clone command for the complete `robocoop` workspace.

### Before installing Self Improvement Learning

- [ ] Access to `unidog_nav`, its submodule, and a dated copy of intended local source changes.
- [ ] A sample JPEG folder for the first mock check. This check needs no robot or model.
- [ ] Before connecting real hardware: the owner-provided robot image/environment, `LLM_guided_RL` deployment, SSH access, camera settings, and demonstrated stop procedure.

A new workstation can complete the mock check while robot preparation is pending. Qwen and NaVILA are [optional model installations](../unidog-nav/models.md). The D1 arm is included in the platform, but its [commissioning guide is pending](../unidog-nav/d1-arm.md).

**Missing something?** Ask your lab contact for the items above before the affected step. The [maintainer's handoff inventory](sources.md) gives the exact folders and unresolved requirements. Keep credentials and device identities in the private setup note.

### Before installing ABC Box

- [ ] Confirm the full Box package, leader type, cameras, and supplied computer image.
- [ ] Get the approved I2RT source revision, device configuration, and operator calibration procedure.
- [ ] Choose `<ABC_DIR>` and `<ABC_DATA_DIR>` on the recording computer.

Follow [Install and rehearse](../abc-box/install.md); the xArm and Go2 environments are not required.

## 3. Learn the few terms used in the steps

| Term | Meaning here |
|---|---|
| Terminal | A window where you type commands. On Ubuntu, open the Terminal app. |
| Repository / repo | A folder of source code, usually downloaded using Git. |
| Environment | A separate collection of Python and its packages. Activating one selects the tools for that part of the system. |
| Server | A program that stays running and waits for requests from another program. Keep its terminal open. |
| IP address | A device's address on the network. Obtain yours from the person configuring the equipment. |
| Port | A numbered connection used by a server, such as `8000`. |
| `localhost` / `127.0.0.1` | The computer on which the command or browser runs. It changes meaning when you switch computers. |
| SSH | A way to log into another computer. An SSH tunnel carries a connection through that login. |
| YAML | A settings file. Indentation matters; use spaces rather than tabs. |
| Policy / model | Software that predicts an action from images, robot state, and a task description. |
| Checkpoint | The saved files containing a trained model. |
| Episode / dataset | One recorded attempt / a collection of recorded attempts. |
| Mock | A software rehearsal using pretend hardware. It does not establish that a real robot is ready. |
| Inference | Asking a trained model to predict an action. Depending on the selected mode, the program may also execute it. |

## 4. Read command blocks correctly

Choose your installation locations using [Choose your folders](paths.md). Directory placeholders such as `<RECORDING_DIR>` and `<NAV_DIR>` always refer to those choices, not the original lab desktops.

- Copy one block at a time, then read the result before continuing.
- `cd` changes the folder. `~` means your home folder on the current computer.
- Text such as `<ARM_IP>` is a placeholder. Replace it, including the angle brackets, before running a command.
- A line ending in `\` continues onto the next line. Copy the whole block.
- A line beginning with `#` is an explanation.
- **Terminal A** and **Terminal B** mean separate terminal windows on the same workstation. Activate the stated environment in each one.
- If a command reports an error, stop at that step. Later steps usually depend on it.

A **workstation** is the Linux computer running the project software. VLA Pipeline and Self Improvement Learning commands run there unless a step says **on the robot**. ABC Box commands run on its **recording computer**, as identified on its pages. Your laptop can display this guide or connect to the workstation using SSH.

Check which computer and folder you are using:

```bash
hostname
pwd
```

**Expected:** the intended computer name and working folder. To leave an SSH login, type `exit`.

## 5. Arrange the first hardware session

Have an experienced operator show you the physical stop control and the manufacturer's power-on/shutdown procedure for your exact robot. The arm's reset command itself moves the arm. The dog's first movement can include standing up. Keep people, cables, and loose objects out of the movement area.

A software stop requires working software and a connection. Learn the physical stop procedure before enabling motion. During headset use, have a second person watch the arm and its surroundings.

**Next:** [Gather the hardware](hardware.md), then [prepare the shared computer](computer.md).
