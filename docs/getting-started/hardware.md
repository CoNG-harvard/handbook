# Shared computer and project hardware

VLA Pipeline and Self Improvement Learning use **one Linux workstation with one RTX PRO 6000 Blackwell Workstation Edition, 96 GB**. Count the computer and its accessories once; keep each project's robot equipment on its own list.

## Shared equipment — prepare once

| Shared equipment | Quantity |
|---|---|
| Complete Linux workstation with RTX PRO 6000 | 1 workstation, 1 GPU |
| Monitor, keyboard, and mouse | 1 set, or arranged remote access |
| Storage and backup destination | Capacity for both projects |
| Network switch/router, power adapter, and workstation cable | 1 suitable set; reuse existing equipment |

The workstation runs either project's software and model. Its storage holds separate source folders, model files, and recordings. The shared network connects the workstation to the selected robot equipment.

Have the supplier include a compatible motherboard, power supply, case, cooling, and mains lead. The inventory does not establish exact parts for these components.

## What each platform needs

Each project has its own equipment list. The two existing projects share the workstation; ABC Box includes a separate recording computer.

### VLA Pipeline: the arm station {#robocoop-the-arm-station}

<figure class="handbook-figure" markdown="1">

![Real lab photo labeled with the xArm, gripper, Quest headset, task objects, mounting stand, control boxes, and stop buttons.](../vla-pipeline/assets/system_overview-labeled.svg)

<figcaption markdown="1">

VLA Pipeline lab station with two xArm 7 robots. Validate each rig separately before using both together.

[View full-size image](../vla-pipeline/assets/system_overview-labeled.svg) · [Source photograph](../vla-pipeline/assets/system_overview.jpg)
{ .figure-links }

</figcaption>

</figure>

[Arm equipment list and wiring steps](../vla-pipeline/hardware/index.md)

### Self Improvement Learning: the navigation robot {#unidog-the-navigation-robot}

<figure class="handbook-figure" markdown="1">

![Self Improvement Learning platform photograph labeled with the Unitree Go2, Unitree D1 arm, and D435i camera.](../unidog-nav/assets/platform.png)

<figcaption markdown="1">

Self Improvement Learning platform with a D1 arm and D435i camera. The first navigation steps do not use arm control.

[View full-size image](../unidog-nav/assets/platform.png) · [Source PDF](../unidog-nav/assets/platform.pdf)
{ .figure-links }

</figcaption>

</figure>

[Self Improvement Learning equipment list and connections](../unidog-nav/hardware.md) — includes one Unitree Go2 and one Unitree D1 arm.

The dog still needs its onboard computer; the arm still needs its control box. Both remain on their project's equipment list.

### ABC Box: leader-controlled teleoperation

The [ABC Box equipment list](../abc-box/hardware.md) separates the full Box package from accessories to confirm with the supplier. Its recording computer is part of that station; count the shared RTX PRO 6000 only once if later used for ABC model work.

[Start the ABC Box guide](../abc-box/index.md).

## Workstation specification for VLA Pipeline and Self Improvement Learning

| Component | Selected configuration or reference |
|---|---|
| GPU | **RTX PRO 6000 Blackwell Workstation Edition, 96 GB** |
| Operating system | Ubuntu 24.04, x86-64, with a Blackwell-compatible NVIDIA driver |
| CPU reference | AMD Ryzen 9 7950X, 16 cores / 32 threads |
| System RAM reference | About 94 GiB reported by Linux; not a tested minimum |
| Storage reference | Two WD_BLACK SN850X 2 TB SSDs and one WD 4 TB hard drive |
| Connections | Ethernet for both arm controllers; USB capacity for five arm cameras, up to two headsets, and input devices |

CPU, RAM, storage, and GPU were inspected on the arm workstation on 24 September 2026. They provide a reference configuration; the projects have not yet been migrated onto one machine. GPU memory and system RAM are separate. Choose storage capacity for your models and recordings, allowing room for backups.

NVIDIA lists 96 GB GPU memory for the [RTX PRO 6000 Blackwell family](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/). Specify the **Workstation Edition**, and have the supplier size power and cooling for it.

## Choosing a new computer

- **Recording:** check USB bandwidth with the cameras and headsets used in the session connected; the full lab station has two D405 cameras, three D415 cameras, and two headsets. Extra ports do not necessarily add bandwidth. The dog's camera connects to its onboard computer.
- **Running models:** validate openpi and Qwen on the selected GPU. NaVILA needs a [Blackwell-compatible environment](../unidog-nav/models.md#navila-installation-and-saved-image-check).
- **Training:** confirm model, dataset, memory, and storage requirements with the model owner before ordering.

## Using the shared workstation

Keep separate folders and [software environments](computer.md): `<RECORDING_DIR>` for arm recording, `<INFERENCE_DIR>` for arm inference, and `<NAV_DIR>` for the dog.

**Run one model service at a time initially.** Both openpi and Qwen use port **8000** by default. GPU capacity alone does not prevent that conflict.

When switching projects:

1. Finish the robot session and follow its shutdown steps.
2. Stop your model and camera services after confirming nobody else needs them.
3. Open the next project's folder and activate its environment.
4. [Select the RTX PRO 6000](computer.md#select-the-rtx-pro-6000-for-model-programs), start the intended model, and complete its health/model check.

Stop openpi before using Self Improvement Learning's all-services launcher: it may reuse a service already listening on port 8000. A response on that port does not prove the correct model is running. Simultaneous operation requires distinct ports and validation of GPU, USB, and network capacity.

## Shared setup checklist

- [ ] One complete workstation, its accessories, storage, and network connection are ready.
- [ ] The [arm equipment list](../vla-pipeline/hardware/index.md) and [dog equipment list](../unidog-nav/hardware.md) are complete.
- [ ] Cameras, cables, addresses, and recordings are labeled by project.
- [ ] Separate environments and the workstation handover procedure are ready.

## Before placing an order

Confirm robot editions, included accessories, software access, cables, and mounts with the owner/vendor. Mark unspecified custom parts **to be specified**; a product name alone is not a complete equipment package.

**Next:** [Prepare the computer](computer.md), then follow the selected project's hardware and installation guide.
