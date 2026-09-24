# Historical findings and open work

These notes summarize lab experiments from **July 2026**. They are not acceptance tests for a new workstation or robot. Use the [current setup guide](index.md) for installation and operation.

## What the earlier experiments found

| Finding | Scope |
|---|---|
| Explicit turn directions improved NaVILA predictions | July 9 scene tests; free-form object goals often produced “move forward” |
| Image history changed the result | Repeated stationary frames biased predictions; see [offline evaluation](vla-eval.md) |
| Closed-loop rollout ran on the robot | July 12 navigation experiment; see [legacy rollout](rollout.md) |
| Short turns exposed timing limits | Gait startup consumed much of the small-turn timeout; requires skills-side tuning |

Historical backend names and restart instructions have been superseded. Use [bridge setup](robot-bridge.md) and [first supervised movement](first-run.md); leave failure-continuation options off during initial validation.

## Open work

- **Instruction grounding:** translate a goal into explicit directions, recheck the target after movement, and determine when the task is complete.
- **Model compatibility:** validate openpi, Qwen, and NaVILA environments on the shared RTX PRO 6000; measure memory use before attempting concurrent models.
- **Distance-aware stopping:** add a validated distance check when a task requires a specific stopping distance.
- **Reproducible installation:** release the lab source bundles, dependency locks, and robot image, then complete a fresh-computer and supervised hardware test.

See [source handoff and verification](../getting-started/sources.md) for the current release requirements.
