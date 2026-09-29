---
title: ABC Box hardware
---

# ABC Box hardware

**Goal:** identify and assemble one complete station from the delivered package plus the parts listed below, and connect it to the [workstation](../getting-started/hardware.md).

[Identify the parts in the labeled photograph](index.md).

## 1. Equipment

Confirm the order is the full **ABC Box**, not the Research Kit. The package list does not explicitly include cameras, leaders, or power supplies. Check the delivered packing list before ordering extras. Workstation, display, and network equipment are counted once in [shared equipment](../getting-started/hardware.md#shared-equipment).

### Included in the Box package

| Equipment | Quantity | Product or reference |
|---|---|---|
| Follower arm with gripper and mounting hardware | 2 | [ABC Box package](https://i2rt.com/products/abc-box) |
| D405 camera mounts (2 wrist, 1 overhead) | 1 kit | [ABC Box camera-mount kit](https://i2rt.com/products/abc-box) |
| Included Box PC and touchscreen | 1 | [ABC Box package](https://i2rt.com/products/abc-box) — keep on the packing list; see connection map |
| Control interface cable and quick-start guide | 1 set | [ABC Box package](https://i2rt.com/products/abc-box) |

### Additional equipment to account for

These are station requirements; obtain only what is missing from the delivered package.

| Equipment | Quantity | Product or reference |
|---|---|---|
| Camera support frame | 1 | [ABC assembly reference](https://abc.bot/hardware.html) — match the delivered station; check whether it is supplied |
| Power supplies and power cords | Supplier-specified set | [I2RT hardware guidance](https://doc.i2rt.com/products/yam-cell) — match the follower and leader models; verify ratings and inclusion |
| Leader arm with handle | 2 | [I2RT leader options](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md) — passive or powered; model to confirm |
| RealSense D405 camera | 3 | [RealSense D405](https://www.realsenseai.com/product-family/d405-series/) |
| Camera USB data cable | 3 | [USB cable catalog](https://www.startech.com/en-us/cables/usb-30) — match connector, length, and bandwidth |
| CAN interface for each follower and leader | 4 (1 per arm) | [I2RT interface reference](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md) — two small adapter boards are fitted at the follower bases; count external adapters with the supplier |
| Work surface, zip ties, and lighting | 1 station | [Workbench](https://www.mcmaster.com/products/workbenches/) · [zip ties](https://www.amazon.com/dp/B08TVLYB3Q) · [work lights](https://www.mcmaster.com/products/work-lights/) |
| Task objects and recording storage | As needed | [Task-area reference](https://abc.bot/hardware.html) · [shared storage](../getting-started/hardware.md#shared-equipment) |

### Notes on selection

- **Leaders:** a passive leader (I2RT's GELLO) only measures joint position; a powered leader (YAM) has motors and its own power supply and needs a different setup. Confirm the delivered model, its power, calibration procedure, and follower compatibility with the supplier.
- **Cameras:** the layout follows the [ABC assembly guide](https://abc.bot/hardware.html) — one D405 at each wrist and one overhead. Follow the delivered Box's own instructions rather than buying the full build-your-own list from that guide.
- **CAN interfaces:** each arm needs one CAN link to a computer (see [glossary](../getting-started/glossary.md)). Four channels do not necessarily mean four external adapters; identify what is already fitted first.
- **Stop:** the [product page](https://i2rt.com/products/abc-box) describes a hardware emergency stop. Have the supplier demonstrate what it cuts and how to restart.

## 2. Connection map

<div class="connection-map" markdown="1">
<div class="connection-hub" markdown="1">

**Workstation + included Box PC — plan to confirm with the supplier**

</div>
<div class="connection-branches" markdown="1">
<div class="connection-branch connection-branch--pending" markdown="1">

**Camera USB → host computer to confirm**

- Left-wrist D405
- Right-wrist D405
- Overhead D405

</div>
<div class="connection-branch connection-branch--pending" markdown="1">

**CAN interfaces → connections to confirm**

- Left leader and left follower
- Right leader and right follower

</div>
</div>
</div>

Both dashed boxes need the supplier's connection plan: which computer receives the cameras and arm interfaces, and which functions stay on the included Box PC. Do not bypass or remove the Box PC without that plan. Record the actual adapter, cable, and port for each arm.

## 3. Assemble and connect

1. **Mount:** secure the followers on the base plate, the leaders at the operator's position, and the camera frame, using the delivered instructions.
2. **Pair and label:** label each leader and follower **left** or **right** and confirm the pairing before enabling movement.
3. **Control connections:** connect the CAN interfaces and computers per the supplier's plan. Label both cable ends and photograph the ports.
4. **Cameras:** mount and label the left-wrist, right-wrist, and overhead D405s and connect them to the host computer in that plan.
5. **Inspect:** check cable clearance, power connections, and the stop location.

## 4. Record identities

| Item | What to record |
|---|---|
| Followers and leaders | Model, serial, left/right pairing, and interface used |
| Cameras | Serial, position, and host computer |
| Computers | Which functions run on the workstation and on the included Box PC |
| Stop | Location, what it cuts, and the restart procedure |

**Next:** [Basic software](software.md)
