# Optional model setup

**Run on the shared Linux workstation.** Complete the [mock check](setup.md) first. You can finish the [live camera check](robot-bridge.md) and [first supervised direct movement](first-run.md) without a model. Return here for language/image planning or offline evaluation.

**Validation status:** package versions and launcher settings were checked against the source workstation on 24 September 2026. Neither Qwen nor NaVILA has been validated on a fresh RTX PRO 6000 installation by this handbook review.

## Choose a model

| Model | Purpose | Environment |
|---|---|---|
| Qwen3-VL | Current language/image planning and voice workflows | `~/unidog_nav/agent_ai/.venv`, Python 3.12 |
| NaVILA | Navigation predictions and existing offline evaluations | Conda environment `navila`, Python 3.10 |

You do not need either model to check the real camera bridge or send a supervised direct command. Install the model used by your intended workflow. The selected GPU is RTX PRO 6000 Blackwell with 96 GB memory. Validate one model at a time before planning concurrent services.

## Qwen installation and check

Select the card using [GPU selection](../getting-started/computer.md#select-the-rtx-pro-6000-for-model-programs). The launcher expects a specific CUDA package layout in Python 3.12. The source environment reports Torch **2.11.0+cu130**. These are **observed versions, not a validated Blackwell lockfile**; obtain the maintainer's full dependency snapshot if installation or the GPU check fails.

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

## NaVILA installation and saved-image check

The bundled `environment_setup.sh` installs Torch 2.3, a CUDA 12-era FlashAttention wheel, and patched Transformers. **Do not use that legacy installer as the RTX PRO 6000 setup recipe.** A newer GPU does not make those old compiled packages compatible.

Have the maintainer supply a Blackwell-compatible `navila` environment, including matching Torch/CUDA/FlashAttention builds and the required NaVILA patches. Updating Torch alone is not a verified migration. Until that environment is provided, complete the mock/bridge setup and validate the optional Qwen environment separately before using it for model work.

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

**Next:** use [offline evaluation](vla-eval.md) for NaVILA, or the [voice and benchmark reference](operator-cookbook.md) for an already commissioned robot.
