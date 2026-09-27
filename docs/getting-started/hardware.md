# Shared computer and hardware

VLA Pipeline, Self Improvement Learning, and ABC Box use **one Linux workstation with one RTX PRO 6000 Blackwell Workstation Edition GPU (96 GB)**. Count the computer and its accessories once; each project's robot equipment is on its own list.

## Shared equipment

| Equipment | Quantity | Product or reference |
|---|---|---|
| Linux workstation with RTX PRO 6000 | 1 | [NVIDIA RTX PRO 6000 family](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/) — complete build to specify |
| Monitor, keyboard, and mouse | 1 set, or remote access | [Monitors](https://www.dell.com/en-us/shop/pc-accessories/ar/computer-monitors) · [keyboards](https://www.logitech.com/en-us/shop/c/keyboards) · [mice](https://www.logitech.com/en-us/shop/c/mice) |
| Storage and backup destination | Sized for all three projects' recordings | [SN850X](https://www.sandisk.com/en-us/products/ssd/internal-ssd/wd-black-sn850x-nvme-ssd) · [hard drives](https://www.westerndigital.com/products/hdd/internal-hdd) — backup device to specify |
| Network switch/router, power adapter, and workstation cable | 1 set | [Switches](https://www.netgear.com/business/wired/switches/unmanaged/) · [Ethernet cables](https://www.startech.com/en-us/cables/network) |
| Assembly tools: hex key set and digital angle gauge | 1 each | [Hex key set](https://www.amazon.com/dp/B0776C2D6H) · [Digital angle gauge](https://www.amazon.com/dp/B0D65VNWPH) — for fastening and leveling arm bases, stands, and camera mounts |

The workstation supplier's quote should include a compatible motherboard, power supply, case, cooling, and mains lead sized for the GPU.

## Workstation specification

| Component | Configuration | Product or reference |
|---|---|---|
| GPU | **RTX PRO 6000 Blackwell Workstation Edition, 96 GB** | [NVIDIA product family](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/) — select Workstation Edition |
| Computer type | Linux workstation; the reference machine runs Ubuntu 24.04 | Complete build to specify |
| CPU (reference) | AMD Ryzen 9 7950X, 16 cores | [AMD Ryzen 9 7950X](https://www.amd.com/en/products/processors/desktops/ryzen/7000-series/amd-ryzen-9-7950x.html) |
| System memory (reference) | About 94 GB | [Memory compatibility catalog](https://www.kingston.com/en/memory) — exact modules not recorded |
| Storage (reference) | Two 2 TB WD_BLACK SN850X SSDs and one 4 TB WD hard drive | [SN850X](https://www.sandisk.com/en-us/products/ssd/internal-ssd/wd-black-sn850x-nvme-ssd) · [WD hard drives](https://www.westerndigital.com/products/hdd/internal-hdd) — HDD model not recorded |
| Connections | Ethernet for the xArm control boxes and robot network; USB for the active platform's cameras, headsets, and control interfaces | [Ethernet](https://www.startech.com/en-us/cables/network) · [USB cables](https://www.startech.com/en-us/cables/usb-30) |

The GPU is the selected configuration. CPU, memory, and storage describe the existing reference machine, not tested minimums; agree capacities with the project owner before ordering a new computer. GPU memory and system memory are separate.

## Choosing a new computer

- **USB bandwidth:** the workstation must stream every camera of the active platform at once — five cameras and up to two headsets for VLA Pipeline, three cameras plus arm interfaces for ABC Box. Several USB sockets can share one internal connection, so more sockets do not always mean more bandwidth. Have the installer check all intended views together.
- **Power and cooling:** the supplier confirms the complete build supports the RTX PRO 6000.
- **Memory and storage:** allow room for recordings and a separate backup destination.

## Using the shared workstation

Arrange use with the other project teams. Before switching platforms, finish the current session with its operator, follow the equipment's shutdown procedure, and confirm nobody else is using the connected devices. Label camera, controller, and network cables by platform.

## Shared setup checklist

- [ ] One complete workstation, its accessories, storage, and network connection are ready.
- [ ] Equipment is checked against the [xArm](../vla-pipeline/hardware/index.md), [Go2/D1](../unidog-nav/hardware.md), or [ABC Box](../abc-box/hardware.md) list.
- [ ] Cameras, cables, and device identities are labeled and recorded.
- [ ] Workstation access and the handover procedure are agreed.

**Next:** [Prepare the workstation](computer.md)
