# Shared computer and project hardware

VLA Pipeline, Self Improvement Learning, and ABC Box use **one Linux workstation with one RTX PRO 6000 Blackwell Workstation Edition, 96 GB**. Count the computer and its accessories once; keep each project's robot equipment on its own list.

## Shared equipment — prepare once

| Shared equipment | Quantity |
|---|---|
| Complete Linux workstation with RTX PRO 6000 | 1 workstation, 1 GPU |
| Monitor, keyboard, and mouse | 1 set, or arranged remote access |
| Storage and backup destination | Capacity for recordings and backups across all three projects |
| Network switch/router, power adapter, and workstation cable | 1 suitable set; reuse existing equipment |

The shared network connects the workstation to the selected robot equipment. Keep enough storage for the planned recordings and a separate backup destination.

Have the supplier include a compatible motherboard, power supply, case, cooling, and mains lead. The inventory does not establish exact parts for these components.

## What each platform needs

All three projects share the same desktop workstation. Gather the robot equipment from the relevant list below.

### VLA Pipeline: the arm station {#robocoop-the-arm-station}

<figure class="handbook-figure" markdown="1">

![Labeled xArm station: both xArm robots; foreground gripper; three D435 scene cameras; two D405 wrist cameras.](../vla-pipeline/assets/xarm-station-labeled.svg){ loading=lazy width=1000 height=750 }

<figcaption markdown="1">

Both xArm robots · Foreground gripper · RealSense D435 (3) · RealSense D405 (2).

Lab photograph provided in September 2026. Labels identify visible parts, not rig A/B assignments.

[View full-size image](../vla-pipeline/assets/xarm-station-labeled.svg) · [Source photograph](../vla-pipeline/assets/xarm-station.jpg)
{ .figure-links }

</figcaption>

</figure>

[Arm equipment list and wiring steps](../vla-pipeline/hardware/index.md)

### Self Improvement Learning: the navigation robot {#unidog-the-navigation-robot}

<figure class="handbook-figure" markdown="1">

![Self Improvement Learning platform photograph labeled with the Unitree Go2, Unitree D1 arm, front D435i camera, and D435 wrist camera.](../unidog-nav/assets/platform-labeled.svg)

<figcaption markdown="1">

The picture shows **1 Go2**, **1 D1 arm**, the labeled front **D435i**, and **1 D435 wrist camera beside the gripper**. The arm requires its own mounting and calibration checks.

[View full-size image](../unidog-nav/assets/platform-labeled.svg) · [Source PDF](../unidog-nav/assets/platform.pdf)
{ .figure-links }

</figcaption>

</figure>

[Self Improvement Learning equipment list and connections](../unidog-nav/hardware.md) — includes one Unitree Go2 and one Unitree D1 arm.

The dog still needs its onboard computer; the arm still needs its control box. Both remain on their project's equipment list.

### ABC Box: leader-controlled teleoperation

<figure class="handbook-figure" markdown="1">

![Labeled ABC Box station: both robot arms; two RealSense D405 cameras at the wrists; one RealSense D405 overhead; camera frame.](../abc-box/assets/abc-box-station-labeled.svg){ loading=lazy width=1000 height=750 }

<figcaption markdown="1">

Both robot arms · RealSense D405 (2 at the wrists, 1 overhead) · Camera frame.

Lab photograph provided in September 2026. The leaders, computer, and stop control are not identified in this view.

[View full-size image](../abc-box/assets/abc-box-station-labeled.svg) · [Source photograph](../abc-box/assets/abc-box-station.jpg)
{ .figure-links }

</figcaption>

</figure>

The [ABC Box equipment list](../abc-box/hardware.md) separates the full Box package from accessories to confirm with the supplier. ABC Box uses the same RTX PRO 6000 workstation as the other two projects; count the desktop once.

[Start the ABC Box guide](../abc-box/index.md).

## Shared workstation specification {#workstation-specification-for-vla-pipeline-and-self-improvement-learning}

| Component | Selected configuration or reference |
|---|---|
| GPU | **RTX PRO 6000 Blackwell Workstation Edition, 96 GB** |
| Computer type | Linux workstation, x86-64; reference machine uses Ubuntu 24.04 |
| CPU reference | AMD Ryzen 9 7950X, 16 cores / 32 threads |
| System RAM reference | About 94 GiB reported by Linux; not a tested minimum |
| Storage reference | Two WD_BLACK SN850X 2 TB SSDs and one WD 4 TB hard drive |
| Connections | Ethernet for the xArm controllers and robot network; USB/data connections for the active platform's cameras, headsets, control interfaces, and input devices |

CPU, RAM, storage, and GPU were inspected on the arm workstation on 24 September 2026. They provide a reference configuration for the desktop shared by all three projects. GPU memory and system RAM are separate. Choose storage capacity for the planned work, allowing room for recordings and backups.

NVIDIA lists 96 GB GPU memory for the [RTX PRO 6000 Blackwell family](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/). Specify the **Workstation Edition**, and have the supplier size power and cooling for it.

## Choosing a new computer

- **Cameras and headsets:** plan USB bandwidth for the active platform: VLA Pipeline has two D405 wrist cameras, three D435 cameras, and up to two headsets; ABC Box has three D405 cameras and its arm-control interfaces. Extra sockets do not necessarily add bandwidth. The dog's camera connects to its onboard computer.
- **Power and cooling:** have the supplier confirm the complete workstation supports the selected RTX PRO 6000 card.
- **Memory and storage:** agree capacity with the project owner before ordering; the values above describe a reference machine rather than tested minimums.

## Using the shared workstation

Arrange use of the workstation with the other project teams. Before switching platforms, finish the current session with its operator, follow the equipment's shutdown procedure, and confirm nobody else is using the connected devices. Keep camera, controller, and network cables labeled by platform.

## Shared setup checklist

- [ ] One complete workstation, its accessories, storage, and network connection are ready.
- [ ] Equipment is checked against the [xArm](../vla-pipeline/hardware/index.md), [Go2/D1](../unidog-nav/hardware.md), or [ABC Box](../abc-box/hardware.md) list as applicable.
- [ ] Cameras, cables, and device identities are labeled and recorded.
- [ ] Workstation access and the equipment handover procedure are agreed.

## Before placing an order

Confirm robot editions, included accessories, cables, mounts, and power requirements with the owner/vendor. Mark unspecified custom parts **to be specified**; a product name alone is not a complete equipment package.

**Next:** [Prepare the workstation](computer.md), then follow the selected project's equipment and connections guide.
