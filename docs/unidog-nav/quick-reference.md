# Quick reference — everyday commands

All run on the **workstation** from the repo root (`~/unidog_nav`). Robot commands need the dog powered on; the other pages in this manual have the details.

```bash
# --- connection & dog-side server -------------------------------------------
ssh -f -N -L 8766:127.0.0.1:8766 unitree            # open the tunnel (once per boot)
python3 scripts/robot_client.py health              # is the bridge up? mock or real?
ssh unitree 'tail -20 ~/logs/primitive_server.log'  # dog-side server log
ssh unitree 'pkill -f "[s]kill_server"; true'       # stop the server (run alone, see note)
ssh unitree 'nohup python3 ~/unidog_nav_tools/primitive_server.py > ~/logs/primitive_server.log 2>&1 < /dev/null &'         # start SAFE: real camera, mock executor
ssh unitree 'nohup python3 ~/unidog_nav_tools/primitive_server.py --real > ~/logs/primitive_server.log 2>&1 < /dev/null &'  # start REAL: robot can move

# --- one-off robot control (server in --real: robot MOVES) -------------------
python3 scripts/robot_client.py image /tmp/frame.jpg     # grab a live camera frame (never moves)
python3 scripts/robot_client.py start-episode            # next motion plan gets stand + ready-check
python3 scripts/robot_client.py exec "The next action is turn left 15 degrees."
python3 scripts/robot_client.py exec "The next action is move forward 25 cm."
python3 scripts/robot_client.py stop                     # EMERGENCY STOP / abort current plan

# --- autonomy (see "Closed-loop rollout" for the full runbook) ---------------
conda activate navila
python scripts/rollout.py --planner navila --max-steps 10 --continue-on-failure \
    --tag my-test --instruction "Turn right and walk to the orange chair. Stop in front of it."

# --- model diagnostics (GPU only, robot not needed) ---------------------------
python scripts/vqa_probe.py <image.jpg> "Is there an orange chair? Left, center, or right?"
python scripts/batch_navila_eval.py --images frames/real_conjested_room1 --history episode-start \
    --query "Turn left."                                # single-shot action prediction
python3 scripts/navila_to_skills.py "The next action is turn right 45 degree."  # parser only, no GPU
python3 scripts/test_navila_to_skills.py                # parser test suite

# --- Qwen server (GPU-exclusive with NaVILA) ---------------------------------
~/unidog_nav/agent_ai/start_vllm.sh                     # serve Qwen3-VL on :8000 (~80 s)
pkill -f "vllm serve"                                   # stop it; then GPU is free for NaVILA
nvidia-smi --query-gpu=memory.used --format=csv,noheader   # ~15 MiB = GPU free
```

Note on the `pkill` lines: run them as shown, in their own command — combining them with a command that contains the literal text `primitive_server.py` makes `pkill -f` kill that shell itself.
