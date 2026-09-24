# Install the project software

**Run on the Linux GPU workstation shared with VLA Pipeline.** Finish [computer preparation](../getting-started/computer.md) first. Keep the physical robot out of this initial software test.

## 1. Download the workstation repository

Using your authorized GitHub account:

```bash
cd ~
git clone --recurse-submodules https://github.com/CoNG-harvard/unidog_nav.git
cd ~/unidog_nav
git submodule status
```

**Expected:** `repos/NaVILA` appears. A submodule is another repository used inside the main one. If it was not downloaded:

```bash
git submodule update --init --recursive
```

The inspected lab checkout includes uncommitted changes. A new clone retrieves committed code only. Ask for the [dated source handoff](../getting-started/sources.md#dog-platform-files) before assuming every recent feature is available.

## 2. Run a mock bridge with no robot

A mock bridge uses stored images and pretend actions. Use port **18766** for this test so it cannot be mistaken for the normal robot tunnel on 8766.

**Terminal A:**

```bash
cd ~/unidog_nav
python3 robot/primitive_server.py --mock --port 18766 \
  --mock-frames test_frames/real_front_wall1
```

This uses Python's standard library; a GPU model is not needed. If that image folder is absent from your handoff, obtain a sample JPEG folder and use its path after `--mock-frames`.

**Terminal B:**

```bash
cd ~/unidog_nav
python3 scripts/robot_client.py --url http://127.0.0.1:18766 health
python3 scripts/robot_client.py --url http://127.0.0.1:18766 image /tmp/unidog-mock.jpg
```

**Expected:** health reports `"ok": true`, `"backend": "mock"`, and `"real": false`; the second command saves an image. Open `/tmp/unidog-mock.jpg` in the workstation's image viewer. It should show a saved scene, not a live feed.

Stop Terminal A with **Ctrl+C** when finished. Success here checks the client/bridge connection only.

## 3. Choose which model you need

| Model | Purpose | Environment |
|---|---|---|
| Qwen3-VL | Current language/image planning and voice workflows | `~/unidog_nav/agent_ai/.venv`, Python 3.12 |
| NaVILA | Navigation predictions and existing offline evaluations | Conda environment `navila`, Python 3.10 |

You do not need either model to check the real camera bridge or send a supervised direct command. Install the model used by your intended workflow. The selected GPU is RTX PRO 6000 Blackwell with 96 GB memory. Validate one model at a time before planning concurrent services.

### Qwen installation and check

Select the card using [GPU selection](../getting-started/computer.md#select-the-rtx-pro-6000-for-model-programs). The launcher expects a specific CUDA package layout in Python 3.12. These are **observed versions, not a validated Blackwell lockfile**; obtain the maintainer's full dependency snapshot if installation or the GPU check fails.

```bash
cd ~/unidog_nav/agent_ai
uv venv --python 3.12
uv pip install --python .venv/bin/python \
  'vllm==0.24.0' 'torch==2.11.0' 'transformers==5.13.0' \
  'nvidia-cuda-nvcc==13.2.78' 'nvidia-cuda-runtime==13.0.96'
```

**Check:**

```bash
.venv/bin/python -c "import vllm, torch; print(vllm.__version__, torch.__version__); print('CUDA available:', torch.cuda.is_available())"
ls .venv/lib/python3.12/site-packages/nvidia/cu13/bin/nvcc
```

Expect the listed versions, `CUDA available: True`, and the compiler path. If the installed Torch build is not the CUDA 13 build expected by the launcher, ask the maintainer for its package index/constraints. Do not edit the launcher's CUDA paths to conceal a mismatched installation.

Before starting, finish any VLA Pipeline model session and stop its openpi server; it also uses port 8000. Follow the [shared-workstation handover](../getting-started/hardware.md#using-the-shared-workstation). Start the Qwen server in **Terminal A**:

```bash
cd ~/unidog_nav
export CUDA_VISIBLE_DEVICES="<RTX_PRO_6000_GPU_UUID>"
bash agent_ai/start_vllm.sh
```

The first launch may download `Qwen/Qwen3-VL-8B-Instruct`. Wait for loading to finish. In **Terminal B**:

```bash
curl --fail http://127.0.0.1:8000/v1/models
```

**Expected:** a model list containing the served model. The inspected launcher uses a long context and most of the GPU memory. An out-of-memory or cache-capacity error means the server has not started successfully; check other GPU use and the maintainer's settings for your hardware.

Stop the foreground server with Ctrl+C when finished, or leave it running only for a workflow that needs it.

### NaVILA installation and saved-image check

The bundled `environment_setup.sh` installs Torch 2.3, a CUDA 12-era FlashAttention wheel, and patched Transformers. **Do not use that legacy installer as the RTX PRO 6000 setup recipe.** A newer GPU does not make those old compiled packages compatible.

Have the maintainer supply a Blackwell-compatible `navila` environment, including matching Torch/CUDA/FlashAttention builds and the required NaVILA patches. Updating Torch alone is not a verified migration. Until that environment is provided, complete the mock/bridge setup and use the separately validated Qwen path for model work.

After installing the maintained environment, select the card and check it:

```bash
conda activate navila
export CUDA_VISIBLE_DEVICES="<RTX_PRO_6000_GPU_UUID>"
python -c "import torch, transformers, llava; print(torch.__version__, transformers.__version__); print(torch.cuda.get_device_name(0)); x=torch.ones(1, device='cuda'); print((x+x).item())"
```

**Expected:** the selected RTX PRO 6000 is named and the small GPU calculation returns `2.0`. This is a basic runtime check, not a complete model-compatibility test.

Obtain the `navila-llama3-8b-8f` checkpoint through the model handoff and place its contents at:

```text
~/unidog_nav/models/navila-llama3-8b-8f/
  llm/
  mm_projector/
  vision_tower/
```

With Qwen stopped and sample images available:

```bash
cd ~/unidog_nav
export CUDA_VISIBLE_DEVICES="<RTX_PRO_6000_GPU_UUID>"
bash scripts/eval_vla.sh \
  --images "$HOME/unidog_nav/test_frames/real_front_wall1" \
  --query "Turn left." --history episode-start
```

**Expected:** a predicted action and a saved result under `logs/`. This evaluates saved images and does not move the robot. More detail is in [offline evaluation](vla-eval.md).

## Installation checkpoint

You can run the mock client and view a saved image. If you installed a model, its model-list or saved-image test succeeds. Next, [connect the real robot and check its camera](robot-bridge.md).
