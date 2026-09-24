# Operation

How to drive the arm and record episodes from the Meta Quest, once a session is launched ([Setup](setup.md)).

## Enter VR on the headset

1. On the Quest, click **META**.
2. Open the **browser** and go to:
   ```
   https://localhost:8012/?ws=wss://localhost:8012
   ```
3. Click **Enter VR** (to the right of the address bar).

!!! warning "Use `localhost`, not the IP"
    `localhost` routes over the USB `adb` forward (cable). The IP route goes over Wi-Fi, whose delay causes **jittery arm movement** during teleoperation.

!!! note "Look forward when you enter VR"
    Be looking **forward** the moment you enter VR — otherwise there will be an orientation offset during teleoperation.

You should then see the wrist and third-person camera feeds.

## Controller mapping

![Meta Quest controllers with the Trigger, Side, A, and B buttons labeled.](../assets/quest_controllers.png)

Right controller unless noted:

| Input | Effect |
|---|---|
| **B** | Start / end an episode |
| **Side button (grip)** — during teleop | Close the gripper (release to open) |
| **A** — after ending an episode | Reset arm to home |
| **Right trigger** — after ending | **Save** the episode |
| **Left trigger** — after ending | **Discard** the episode |

!!! note
    With the default config the gripper stays pointing straight down, but it still rotates around the z axis (yaw follows your wrist).

## Recording workflow (per episode)

```
 Press A (reset) ─▶ Press B (start; arm follows your hand) ─▶ Press B (stop)
        ▲                                                          │
        │                                          Right trigger = save
        └──────────── Press A (reset) ◀─────────── Left trigger  = discard
```

Press ++ctrl+c++ in the terminal to end the whole session (saved episodes are kept).

## When the arm is stuck

The xArm controller **latches into an error state** on collision, joint-limit, singularity, or overload. Once latched, it rejects every motion command until the error is cleared — and some errors cannot be cleared in software at all; they require a power-cycle of the arm.

### Standard recovery

1. **Press E-stop** on the right control box (the red button).
2. **Release** it — lift up and turn clockwise.
3. **Press A** on the right handle. This resets the xArm and **deletes the last (partial) episode**.

### Alternative recovery

Sometimes **continuously pressing A** recovers the arm without needing the E-stop at all — try this first, and fall back to the E-stop sequence above if it stays stuck.
