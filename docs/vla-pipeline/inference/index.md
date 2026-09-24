# Inference

Running a trained policy on the real xArm. The action source simply switches from the VR operator to the policy — everything else (robot driver, cameras, control loop) is the same plumbing as [teleoperation](../teleop/setup.md).

!!! important "Match training and inference"
    The robot type, camera names/resolutions, and observation/action layout must match what the policy was **trained** on. Reuse the same `--robot.*` and `--robot.cameras` settings you recorded with.

## Method A — run the policy with `lerobot-record` (recommended)

`lerobot-record` accepts a `--policy.path`. With a policy set, the arm is driven by the policy instead of the operator. This is the practical way to run on the real robot — LeRobot handles loading, normalization (pre/post-processing), device placement, and the control loop for you.

```bash
lerobot-record \
    --robot.type=xarm_robot \
    --robot.xarm_ip=<ARM_IP> \
    --robot.cameras='{ wrist_camera: {type: imageclient, host: "<IMG_SERVER_IP>", request_port: 60000, camera_name: wrist_camera, width: 640, height: 480, fps: 30}, right_3pv_camera: {type: imageclient, host: "<IMG_SERVER_IP>", request_port: 60000, camera_name: right_3pv_camera, width: 640, height: 480, fps: 30} }' \
    --policy.path=<HF_USER>/my_policy \
    --dataset.repo_id=<HF_USER>/eval_run \
    --dataset.root=~/lerobot/xr_teleoperate/datasets/eval_$(date +%Y%m%d_%H%M%S) \
    --dataset.single_task="Pick a red cube and put it in the basket" \
    --dataset.fps=30 \
    --dataset.num_episodes=10 \
    --dataset.push_to_hub=false
```

- **`--policy.path`** — a local checkpoint directory (e.g. from training) or a Hugging Face Hub repo id.
- The run still records a dataset (the policy rollouts) under `--dataset.root` — useful for evaluation. Set `--dataset.num_episodes` to how many rollouts you want.
- **Teleop is optional** alongside a policy: add the same `--teleop.*` flags from [Setup](../teleop/setup.md) if you want to take over between episodes (e.g. to reset the scene by hand). Without them, the arm is policy-only.

!!! danger "First autonomous run"
    Keep a hand on the **E-stop**. A freshly trained policy can move unexpectedly. Start with the workspace clear and be ready to stop — the same [recovery flow](../teleop/operation.md#when-the-arm-is-stuck) applies.

## Method B — load and call the policy in Python

For custom loops (debugging, a non-LeRobot integration) you can load the checkpoint directly. Note: unlike Method A, you are responsible for building the observation batch and applying the policy's normalization.

```python
import torch
from lerobot.policies.act.modeling_act import ACTPolicy   # use the class matching your policy

# 1. Load the trained checkpoint (local dir or Hub repo id)
policy = ACTPolicy.from_pretrained("<path_or_repo>")
policy.eval()
policy.to("cuda")

# 2. Reset internal state at the start of each episode
policy.reset()

# 3. Per control step: build the observation batch, get an action
#    `batch` keys must match the policy's expected features
#    (camera images as float tensors + the robot state), already normalized
#    and on the policy's device.
with torch.no_grad():
    action = policy.select_action(batch)   # -> action tensor

# 4. Send `action` to the robot (de-normalized to the robot's units),
#    then read the next observation and repeat.
```

!!! tip "Use the record pipeline as the reference"
    Building `batch` correctly (image preprocessing, state normalization, device) is fiddly. LeRobot's record script wires this up with `make_policy` / `make_pre_post_processors` and a `predict_action` helper — see `lerobot/scripts/lerobot_record.py` in the source. For running on the real xArm, **Method A is strongly preferred** because it reuses that exact, tested path.

## Choosing the policy class

`from_pretrained` is defined on each policy class. Use the one your checkpoint was trained with — e.g. `ACTPolicy` (`lerobot.policies.act.modeling_act`), or another from `lerobot.policies.*` (pi0, pi05, smolvla, vqbet, …). Method A figures this out from the checkpoint config automatically; in Method B you import the matching class yourself.
