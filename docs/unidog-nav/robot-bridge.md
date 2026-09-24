# Workstation ↔ robot bridge

`robot/primitive_server.py` runs on the Go2's onboard PC (stdlib-only) and exposes the camera and the primitive executor over HTTP; `scripts/robot_client.py` is the workstation side. Transport is an SSH tunnel, so nothing is exposed on the WiFi:

```bash
# one-time deploy (dog reachable as `ssh unitree`, <DOG_IP>)
scp robot/primitive_server.py unitree:unidog_nav_tools/

# on the dog: start the server next to the executor (LLM_guided_RL) repo
python3 unidog_nav_tools/primitive_server.py --iface eth0 --skills-repo <path-to-skills-repo>

# on the workstation: keep a tunnel open in a spare terminal
ssh -N -L 8766:127.0.0.1:8766 unitree

# then
python scripts/robot_client.py health
python scripts/robot_client.py image /tmp/frame.jpg
python scripts/robot_client.py start-episode          # next motion plan gets check_robot_ready + stand
python scripts/robot_client.py exec "The next action is move forward 50 cm."
python scripts/robot_client.py stop                   # aborts between calls / stops if idle
```

`POST /plan` executes calls sequentially, prepends the safety prologue before an episode's first motion (`--real` mode only — the mock executor has no safety monitor), aborts on the first non-success `SkillResult`, and returns every per-call result for the replanning loop. Plumbing is testable anywhere with `python3 robot/primitive_server.py --mock` (mock camera serves `frames/`, mock executor returns successes).

**Dog-side integration (deployed & verified live 2026-07-12).** The server does not import the executor library; it shells out to the sanctioned entry points of `~/LLM_guided_RL` (branch `offline-rl-vlm-policy`, the collaborator's repo — nothing in it is modified):

- `scripts/grab_front_frame.py` — one 1920×1080 JPEG via the videohub RPC (~1.3 s; ~1.4 s workstation-to-workstation through the tunnel).
- `scripts/run_skill.py NAME --params JSON` — any registered skill with the repo's own Go2Robot + SafetyMonitor + stand-prep + cleanup wiring; `--real --yes --ip eth0` only when the server runs with `--real`, otherwise their `--mock` (~3.5 s per call, robot untouched). `POST /stop` SIGTERMs the running skill subprocess, which `run_skill.py` converts into a safe abort + `robot.stop()` (same path as their voice-pipeline cancel).

Both subprocesses use the `walk` conda python (`~/miniforge3/envs/walk`, py3.8). Server start on the dog: `python3 ~/unidog_nav_tools/primitive_server.py` (mock executor, real camera) or `... --real` for actual motion.

## Collecting frames (on the dog)

Frames are captured by `~/unidog_nav_tools/collect_navila_images.py` on the Go2's onboard PC (host `ubuntu`), which reads the front camera via the Unitree videohub RPC: 8 frames at 0.3 s intervals per scene, saved with per-frame brightness/saturation stats in `metadata.json`. Copy the resulting folder into `frames/` in the workstation repo (`~/unidog_nav`).
