---
title: ABC Box hardware
---

# ABC Box hardware

**Goal:** identify and assemble one complete station. Use the delivered packing list to confirm inclusion; a camera mount is not a camera.

[Identify the parts in the labeled photograph](index.md) — the two follower arms and three D405 cameras.

The [shared RTX PRO 6000 workstation and its accessories](../getting-started/hardware.md#shared-equipment-prepare-once) serve all three projects and are counted once. ABC Box does not require a separate desktop on this equipment list.

## Photo count check

The photo shows **2 robot arms, 2 grippers, 2 wrist cameras, and 1 overhead camera**: **3 cameras total**, matching the camera quantity below. The support frame is also visible. The picture does not verify the two leaders, shared workstation connections, or stop control; confirm those against the delivered equipment. Camera model names come from the equipment references, not readable model labels in this view.

## 1. Check the ABC Box package

The robot equipment below comes from I2RT's full ABC Box package list. Confirm the order specifies **ABC Box**, rather than the Research Kit. [Manufacturer package list](https://i2rt.com/products/abc-box)

Product links identify known models. **Catalogs** and assembly **references** cover unspecified parts; confirm exact sizes, compatibility, and included accessories before ordering.

| Listed equipment | Quantity | Product or reference |
|---|---|---|
| Follower arm with mounting hardware | 2 | [ABC Box package](https://i2rt.com/products/abc-box) |
| D405 camera mount positions | 3: two wrist, one overhead | [ABC Box camera-mount kit](https://i2rt.com/products/abc-box) |
| Control cable and quick-start guide | 1 package | [ABC Box package](https://i2rt.com/products/abc-box) |

The [full Box package](https://i2rt.com/products/abc-box) also lists a small PC and touchscreen. Keep these included components on the packing list; no additional desktop purchase is listed. Have the supplier confirm how the shared workstation connects, which computer receives the camera and arm cables, and which functions remain on the included PC. Do not bypass or remove it without that plan.

The [ABC Box product page](https://i2rt.com/products/abc-box) describes a hardware emergency stop. Ask the supplier to demonstrate which equipment it cuts off, and the procedure for restarting afterward.

## 2. Confirm the additional equipment

| Equipment needed for this workflow | Quantity | Product or reference |
|---|---|---|
| Compatible leader arms and handles | 2 | [I2RT leader options](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md) — hardware reference; model to confirm |
| RealSense D405 cameras | 3 | [RealSense D405](https://www.realsenseai.com/product-family/d405-series/) |
| Camera USB data cables | 3 | [USB cable catalog](https://www.startech.com/en-us/cables/usb-30) — match connectors, length, and bandwidth |
| Working communication connection for each follower and leader | 4 channels | [I2RT interface reference](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md) — confirm supplied adapters |
| Matching grippers, power supplies, and mains leads | Confirm the complete supplied set | [I2RT package](https://i2rt.com/products/abc-box) · [assembly reference](https://abc.bot/hardware.html) — confirm included parts |
| Stable work surface, cable restraints, and lighting | 1 station | [Workbench](https://www.mcmaster.com/products/workbenches/) · [cable ties](https://www.mcmaster.com/products/cable-ties/) · [lighting](https://www.mcmaster.com/products/work-lights/) — catalogs |
| Task objects and backup storage | As needed | [Task-area reference](https://abc.bot/hardware.html) · [shared storage](../getting-started/hardware.md#shared-equipment-prepare-once) |

**Leaders and cameras:** their inclusion is not explicit in the ABC Box package list. Get written confirmation before ordering extras. The [ABC assembly guide](https://abc.bot/hardware.html) uses two wrist D405s and one overhead D405. Follow the delivered Box's assembly instructions rather than buying all parts from that separate, build-your-own station list.

**Leader choice matters:** passive GELLO leaders measure joint position without driving motors; powered YAM leaders need a different setup. Have the supplier confirm the actual leader model, its power requirements, calibration procedure, and compatibility with the followers. [I2RT hardware configuration](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md)

**Communication:** CAN is a communication link used by the arm control equipment. Have the supplier identify each supplied interface before purchasing adapters; do not assume all four require an additional external adapter.

## 3. Connect and label the station

### Connection map

<div class="connection-map" markdown="1">
<div class="connection-hub" markdown="1">

**Computer arrangement → supplier confirmation needed**

Shared RTX PRO 6000 workstation + any included Box PC

</div>
<div class="connection-branches" markdown="1">
<div class="connection-branch connection-branch--pending" markdown="1">

**Camera USB → confirm host computer**

- Left-wrist D405
- Right-wrist D405
- Overhead D405

</div>
<div class="connection-branch connection-branch--pending" markdown="1">

**Control interfaces → confirm supplied connections**

- Left leader and left follower
- Right leader and right follower

</div>
</div>
</div>

Both dashed boxes need the supplier's connection plan. Record the actual adapter, cable, and port for each arm; four communication channels do not necessarily mean four external adapters. Power supplies and the physical stop follow the delivered Box instructions.

### Assemble and connect

1. **Mount:** have the installer secure followers, leaders, and the camera frame using the delivered instructions.
2. **Pair:** label each leader and follower **left** or **right**. Confirm the pairing before enabling movement.
3. **Control connections:** have the installer connect the arm interfaces and computers according to the supplier-approved plan. Label both cable ends and photograph the ports.
4. **Cameras:** mount and label the left-wrist, right-wrist, and overhead D405s; connect their USB data cables to the host computer specified in that plan.
5. **Inspect:** check cable clearance, power connections, and the stop location. Save the arrangement in the [station record](../getting-started/station-record.md).

**Check before continuing:** two identified leader/follower pairs, three labeled cameras, documented control interfaces, and an accessible stop. Complete the readiness checks before the first session.

**Next:** [Check hardware readiness](readiness.md) with the installer and operator.
