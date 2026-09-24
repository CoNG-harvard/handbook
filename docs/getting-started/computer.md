# Prepare a new computer

**Run these steps on the shared Linux workstation.** Do them once for both projects. The reference lab machines run Ubuntu 24.04 on x86-64 PCs. This guide does not cover installing the robot stack directly on macOS, Windows, or the dog's ARM computer.

## 1. Prepare Ubuntu and the graphics card

Have your computer administrator install Ubuntu and the NVIDIA driver appropriate for the machine. GPU means graphics processor; the model uses its memory to process images. Use **NVIDIA RTX PRO 6000 Blackwell Workstation Edition, 96 GB**, in the workstation shared by both projects. See the [hardware list](hardware.md) for the rest of the equipment.

Open Terminal:

```bash
uname -m
nvidia-smi
```

**Expected:** `x86_64`, then a table showing the NVIDIA GPU, driver, and memory. If `nvidia-smi` fails, resolve the driver installation before installing model software. Arm teleoperation can be checked before a model is installed.

### Select the RTX PRO 6000 for model programs

List the graphics cards:

```bash
nvidia-smi --query-gpu=name,uuid,memory.total --format=csv
```

Find the **RTX PRO 6000 Blackwell Workstation Edition** row and copy its identifier beginning with `GPU-`. In each terminal that will start a model, set:

```bash
export CUDA_VISIBLE_DEVICES="<RTX_PRO_6000_GPU_UUID>"
```

Replace the placeholder with the full identifier, including `GPU-`. This tells CUDA programs to use that card even when another card is installed. The selection applies to that terminal and programs started from it; repeat it in other model terminals. See [NVIDIA's GPU-selection documentation](https://docs.nvidia.com/deploy/topics/topic_5_2_1.html).

A working `nvidia-smi` does not prove an old Python environment supports Blackwell. The model's PyTorch/JAX/CUDA packages and compiled extensions must also support it. In particular, the legacy NaVILA Torch 2.3/CUDA 12.1 recipe is not a supported fresh-install path for this GPU. [PyTorch introduced Blackwell support in its 2.7 release with CUDA 12.8 builds](https://pytorch.org/blog/pytorch-2-7/); a compatible model environment still needs its own validation.

## 2. Install common tools

The following Ubuntu commands install download tools, Git, a text editor, and system libraries used by the camera software. `sudo` asks for your workstation password; nothing appears while you type it.

```bash
sudo apt update
sudo apt install -y git git-lfs curl wget unzip rsync tmux nano \
  build-essential python3-venv pkg-config ffmpeg openssl \
  libusb-1.0-0-dev libturbojpeg-dev libgl1
```

```bash
git lfs install
git --version
```

**Expected:** Git reports its version without an error.

## 3. Install Conda

Conda lets the projects use different Python versions. Follow the [official Miniconda installation guide](https://www.anaconda.com/docs/getting-started/installation) and choose **Linux x86-64**. Choose an installation folder and record its full path as `<CONDA_DIR>` in the [folder guide](paths.md). The Self Improvement Learning evaluation wrapper contains a deployment-specific Conda path; have the maintainer update it to this location before using that wrapper. Allow the installer to initialize your shell, then close and reopen Terminal.

```bash
conda --version
```

**Expected:** a version number. If the command is missing but you installed in `<CONDA_DIR>`, run:

```bash
source "<CONDA_DIR>/etc/profile.d/conda.sh"
```

## 4. Install uv

The arm model server and the dog's Qwen model use a separate environment manager called **uv**. Download its installer, then run it, following the [official uv instructions](https://docs.astral.sh/uv/getting-started/installation/):

```bash
curl -LsSf https://astral.sh/uv/install.sh -o /tmp/uv-install.sh
sh /tmp/uv-install.sh
```

Reopen Terminal and check:

```bash
uv --version
```

## 5. Check access and storage

Make sure you can download the lab repositories and model files using **your own account**. A `Repository not found`, `401`, or `403` error may mean missing access rather than a bad command. Obtain access from the project owner before retrying.

```bash
df -h ~
```

This shows available disk space. Ask for the checkpoint and sample dataset sizes, and leave additional space for environments, downloaded packages, and recordings. Do not copy the original workstation's entire model or video collection just to run a first test.

## 6. Choose your next page

- **Robot arm:** [assemble and connect the hardware](../vla-pipeline/hardware/index.md), then [install the arm software](../vla-pipeline/install.md).
- **Robot dog:** check the [hardware and connections](../unidog-nav/hardware.md), [install Self Improvement Learning on the workstation](../unidog-nav/setup.md), then connect the robot through the bridge.

Keep the environments separate. `lerobot` is the arm's recording/client environment; openpi has its own `.venv`; `navila` is the dog's older model environment; Qwen has a different `.venv`. A package upgrade in one does not belong in the others.
