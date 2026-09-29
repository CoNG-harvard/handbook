---
hide:
  - footer
---

# TurtleBot3 hardware readiness

**Goal:** hand over a clearly identified robot with working sensors and a demonstrated stop procedure. Complete [basic software](software.md) and read the shared [safety rules](../getting-started/safety.md) first.

## 1. Inspect before power-on

- [ ] Chassis, wheels, boards, and LiDAR are secure.
- [ ] Cables are clear of wheels and the floor.
- [ ] The battery and connectors have no visible damage; the matching charger is available.
- [ ] The operator has shown how to shut down normally and how to stop the robot if communication fails.
- [ ] The test area is level and clear of stairs, table edges, feet, and loose objects.

Use the demonstrated power-on procedure with no motion controller active.

## 2. Check live sensor data

| Check | Ready when |
|---|---|
| Robot identity | The physical label matches the robot being viewed on the computer |
| LiDAR | Scans refresh and show nearby stationary surroundings |
| Odometry and status | Readings arrive with fresh timestamps and no reported device fault |
| Optional OptiTrack | The correct rigid body is tracked, and fresh pose data reaches the receiving computer |

If a check fails, return to [basic software](software.md#3-check-robot-discovery-and-sensors). Do not use motion to discover which robot a controller addresses.

## 3. Supervised first movement

Have an experienced operator follow the matching [ROBOTIS basic-operation guide](https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_operation/). Begin with one robot at low speed in the cleared area. Confirm forward movement, turning, stopping, and the agreed response to loss of control communication.

Before adding another robot, verify separate command routing. Do not rely on an untested keyboard stop or assume a power switch is a dedicated emergency-stop button.

## 4. Handover

Record the installed versions, robot identity, connection method, tested stop procedure, and responsible operator in private setup notes. Remove temporary charging or service leads before driving.

**Ready when:** the operator has approved the hardware, live sensor checks, and supervised stop test.

[Project overview](index.md) · [All projects](../index.md)
