# Run a trained model on the arm

**Goal:** first ask a model to predict actions from saved data, then perform a supervised live trial. You need the installed [arm client software](../install.md), the lab's openpi source, a compatible checkpoint, and a small processed dataset.

The model server predicts actions. `run_xarm_inference.py` is the client that gathers input and, in live mode, sends the predictions to the arm. Both are needed for a live trial.

Configure the client through its YAML file and the **`--config`** option. Older command-line options such as `--task` and `--from-dataset` do not apply to this version.

## 1. Install the model server

**On the arm workstation, in a new terminal:**

```bash
cd "<INFERENCE_DIR>/openpi"
uv venv --python 3.11
GIT_LFS_SKIP_SMUDGE=1 uv sync --frozen
GIT_LFS_SKIP_SMUDGE=1 uv pip install -e . --no-deps
```

Use the supplied lab checkout with its `uv.lock`, not a new upstream checkout with different settings. The selected GPU is **RTX PRO 6000 Blackwell 96 GB**. The maintainer must validate the locked JAX/CUDA/model stack on this card; a successful dependency install alone is not a GPU compatibility test. These commands create `.venv` inside `openpi`. If `uv sync` fails, keep the error and ask the maintainer to check the handed-off source/lockfile pair. Do not silently replace the lockfile with newer dependencies.

Install the lightweight client into the **separate** recording environment:

```bash
conda activate lerobot
python -m pip install -e "<INFERENCE_DIR>/openpi/packages/openpi-client"
python -c "from openpi_client import websocket_client_policy; print('Policy client found')"
```

**Expected:** `Policy client found`.

## 2. Obtain a checkpoint that matches the arm

Ask the model owner for the checkpoint, the openpi configuration name, its task, camera arrangement, image processing, action units, and matching sample dataset. A downloaded generic model is not automatically compatible with this robot. See the [model handoff checklist](../training/index.md).

If the checkpoint is stored on Hugging Face, use the included downloader with the supplied repository and folder:

```bash
cd "<INFERENCE_DIR>"
conda activate lerobot
python models/download_model.py \
  --repo-id "<MODEL_REPOSITORY>" \
  --folder "<CHECKPOINT_SUBFOLDER>"
```

**Expected:** a `Downloaded ... -> ...` message and a local checkpoint directory. Record the full destination path. Access-controlled downloads require your own account authorization. The inspected reference setup uses an xArm-finetuned model with the `pi05_droid_finetune` configuration; confirm that name for your checkpoint.

## 3. Start the model server — Terminal A

Use the full GPU identifier found in [computer preparation](../../getting-started/computer.md#select-the-rtx-pro-6000-for-model-programs).

```bash
cd "<INFERENCE_DIR>/openpi"
export CUDA_VISIBLE_DEVICES="<RTX_PRO_6000_GPU_UUID>"
uv run scripts/serve_policy.py policy:checkpoint \
  --policy.config="<POLICY_CONFIG_NAME>" \
  --policy.dir="<FULL_CHECKPOINT_PATH>"
```

**Expected:** the model finishes loading and the server listens on port **8000**. Keep this terminal open. Model loading can take time; an error traceback is not a ready server. This server starts no arm controller by itself.

The shared workstation also runs Self Improvement Learning. Its Qwen server uses port 8000 too. Finish that project's session and stop its model server before starting openpi. Follow the [shared-workstation handover](../../getting-started/hardware.md#using-the-shared-workstation); simultaneous operation needs distinct ports and separate resource validation.

## 4. Make a saved-data configuration — Terminal B

```bash
cd "<INFERENCE_DIR>"
conda activate lerobot
cp run_xarm_inference.yaml first-check.yaml
nano first-check.yaml
```

Change these values in the **existing complete file**:

| Field | Set it to |
|---|---|
| `policy.host` | `localhost` if Terminal A is on this workstation |
| `policy.port` | `8000`, unless you deliberately changed the server port |
| `run.task` | The instruction associated with the sample episode |
| `mode.name` | `from_dataset` |
| `mode.dataset_dir` | Full absolute path to the processed sample dataset; avoid `~` inside YAML |
| `mode.episode` | A supplied valid episode number, often `0` |
| `mode.sample_idx` | A valid frame number; use `0` for the first check |

Leave the rest of the supplied file intact. Then run:

```bash
python run_xarm_inference.py --config first-check.yaml
```

**Expected:** the program identifies dataset comparison mode, connects to the policy, prints predicted/reference action error measures such as MAE and RMSE, then finishes with `Done.` This mode does **not** connect to the robot in the inspected code. It does not require live cameras.

The numbers show a comparison, not a pass/fail safety threshold. Ask the model owner to review the predictions and action units before a live run.

## 5. Prepare live cameras and settings

Stop teleoperation and any other program controlling the arm. Start the camera server in **Terminal C** if none is running:

```bash
conda activate lerobot
teleimager-server --rs
```

Check the live images as in [camera setup](../teleop/setup.md#3-test-the-cameras-before-moving-the-arm).

Make a separate live configuration:

```bash
cd "<INFERENCE_DIR>"
cp first-check.yaml first-live.yaml
nano first-live.yaml
```

With the operator, review:

- `mode.name: live`.
- `robot.xarm_ip`: this station's arm controller.
- `robot.camera.host`, `request_port`, `wrist_name`, and `exterior_name`: this camera server and its matching topics.
- `run.task`: the supported task for the checkpoint.
- Camera orientation/crop, gripper settings, and action units: must match training.
- `run.max_timesteps`: choose a short initial trial with the operator. At the reference 15 Hz, 30 steps is about two seconds of commanded control; model/network delays add time.
- `control` settings: have the operator check movement limits for this arm and mounting arrangement.

## 6. Perform the supervised trial

!!! warning "This connects to real hardware"
    Starting a live-mode client connects and configures the arm **before** the rollout prompt. The operator must already be at the stop control with the workspace clear.

In **Terminal B**:

```bash
cd "<INFERENCE_DIR>"
conda activate lerobot
python run_xarm_inference.py --config first-live.yaml
```

The inspected live loop asks `Enter to start rollout, Ctrl+C to quit...`. Begin only when the operator is ready. Answer `n` to the next-rollout prompt when finished. Use the physical stop for unexpected motion; Ctrl+C is the normal program exit, not a substitute for the physical stop.

With `run.save_video: true`, rollout videos are written in the working directory. Review the trial with the model owner before increasing its duration.

## Know which modes use hardware

| `mode.name` | First-time use |
|---|---|
| `from_dataset` | Saved-data prediction; verified in source to avoid robot connection |
| `live` | Uses live cameras and controls the arm |
| `replay` | Sends recorded actions to the real arm; it is not a video player |
| `predict_execute` | Predicts from saved observations and executes on the real arm |
| Other diagnostic modes | Advanced only; several connect to hardware even when their names sound offline |

## Troubleshooting and shutdown

| Problem | First check |
|---|---|
| `unrecognized arguments: --task` | Use `--config` and edit the YAML settings |
| Cannot connect to policy | Terminal A finished loading; host and port agree |
| Dataset/frame not found | Absolute path, episode number, and frame index are valid |
| Camera missing or wrong image | Topic names and physical serials agree; only one camera server owns the devices |
| GPU out of memory | Check `nvidia-smi`; coordinate with the owner of other GPU processes |
| Wrong-looking predictions | Stop before live testing; check model/config/data pairing and preprocessing |

End the client before stopping its model server. Stop Terminal A and any camera server you started with Ctrl+C once no other user needs them. Park and shut down the arm according to the operator/manufacturer procedure.
