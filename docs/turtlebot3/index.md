---
title: TurtleBot3 Burger
---

# TurtleBot3 Burger

A compact wheeled robot with a laser distance sensor (**LiDAR**), an onboard Raspberry Pi, and an OpenCR motor-control board. A computer on the same network connects to the robot through **ROS 2**, the software that carries sensor readings and robot commands. Optional OptiTrack equipment measures the robot's position in the room.

**Goal:** check the robot and battery, connect a compatible computer, and confirm live sensor readings before a supervised first drive.

!!! info "What you need"
    **Core equipment:** a complete Burger robot · matching battery and charger · a computer with a matching ROS 2 environment · a shared network.

    **Optional:** the room's OptiTrack system and markers for external position tracking. See [equipment and connections](hardware.md).

!!! note "Station photograph"
    A photograph of the lab's TurtleBot3 setup is not yet available for this guide.

## Set up the platform

| Step | Guide | Ready when |
|---|---|---|
| 1 | [Equipment and connections](hardware.md) | The kit, battery, cables, and network are checked |
| 2 | [Basic software](software.md) | The computer and robot use matching software and live sensor data is visible |
| 3 | [Hardware readiness](readiness.md) | The operator has checked robot identity, stopping, and the driving area |

The documented lab setup uses **Ubuntu 20.04 and ROS 2 Foxy**. Confirm the installed versions before using it; the [software guide](software.md#1-choose-the-matching-environment) explains the legacy setup and the route for a new installation.
