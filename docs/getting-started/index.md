# Before you begin

**Goal:** know what you are setting up and have the information needed to finish. Read this page once before installing anything.

## 1. Choose a project

**VLA Pipeline** is a tabletop setup with two xArm 7 robots. A person can guide it using a Meta Quest headset and controllers. The computer can save the camera images and movements as a demonstration. Later, a trained model can choose movements itself. The hardware list covers **both arms**. Validate rig A first, repeat for rig B, then configure the intended two-arm workflow.

**Self Improvement Learning** uses a Unitree Go2 robot dog with a Unitree D1 arm. A workstation looks at camera images and sends commands to a separate computer carried by the dog. The dog also needs the lab's robot-control software. Installing the workstation software alone does not make an unconfigured dog ready to walk.

Use the [hardware checklist](hardware.md) to gather the full station, including the **RTX PRO 6000 Blackwell Workstation Edition, 96 GB**, in one workstation shared by both projects.

## 2. Get a setup handoff from the lab

Ask the person responsible for the platform for the items below. Save the answers in a **private setup note**. Passwords, access tokens, addresses, and device serial numbers do not belong in this public handbook.

| Information | VLA Pipeline | Self Improvement Learning |
|---|---|---|
| Source files | VLA Pipeline scripts, the modified LeRobot workspace, and the lab openpi fork | `unidog_nav`, its NaVILA submodule, and the robot-side `LLM_guided_RL` code |
| Access | Permission to download lab code, model, and a sample dataset | Permission to download lab code and model; SSH access to the robot |
| Network details | Arm address and camera-server address | Robot computer address, login name, and confirmed SSH host fingerprint |
| Device details | Which arm is rig A; headset and camera serials | Go2 variant, onboard computer, selected camera, and network interface |
| Calibration | Mounting, home position, camera view, gripper setup | Robot readiness/stop procedure; any attached arm's calibration |
| First test | A matching checkpoint and a small processed dataset | A sample image folder and a clear, supervised test area |

The [handoff inventory](sources.md) lists the actual folders. **There is no verified public `robocoop` clone command for the complete workspace.** Obtain the lab files before proceeding; an unrelated repository with the same name will not work.

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

- Copy one block at a time, then read the result before continuing.
- `cd` changes the folder. `~` means your home folder on the current computer.
- Text such as `<ARM_IP>` is a placeholder. Replace it, including the angle brackets, before running a command.
- A line ending in `\` continues onto the next line. Copy the whole block.
- A line beginning with `#` is an explanation.
- **Terminal A** and **Terminal B** mean separate terminal windows on the same workstation. Activate the stated environment in each one.
- If a command reports an error, stop at that step. Later steps usually depend on it.

A **workstation** is the Linux computer running the project software. Commands run there unless a step says **on the robot**. Your laptop can display this guide or connect to the workstation using SSH.

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
