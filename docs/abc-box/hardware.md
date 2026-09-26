# ABC Box hardware

**Goal:** identify and assemble one complete station. Use the delivered packing list to confirm inclusion; a camera mount is not a camera.

<figure class="handbook-figure" markdown="1">

![Labeled ABC Box station: both robot arms; two RealSense D405 cameras at the wrists; one RealSense D405 overhead; camera frame.](assets/abc-box-station-labeled.svg){ loading=lazy width=1000 height=750 }

<figcaption markdown="1">

Both robot arms · RealSense D405 (2 at the wrists, 1 overhead) · Camera frame.

Lab photograph provided in September 2026. The leaders, computer, and stop control are not identified in this view.

[View full-size image](assets/abc-box-station-labeled.svg) · [Source photograph](assets/abc-box-station.jpg)
{ .figure-links }

</figcaption>

</figure>

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

The [full Box package](https://i2rt.com/products/abc-box) also lists a small PC and touchscreen. Keep any included units on the delivered packing list; the lab uses the shared desktop, so do not count a second desktop as a requirement. Have the supplier confirm the shared workstation's physical connection to the supplied control interfaces.

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

1. Have the installer secure the follower and leader mounts using the supplied instructions.
2. Label left/right followers, their paired leaders, and each control cable. Have the installer connect the supplier-approved control interfaces to the shared workstation.
3. Mount and label the top, left-wrist, and right-wrist cameras; connect them to the shared workstation.
4. Route power and data cables clear of joints and the work area.
5. Record device identities, approved resting poses, and the stop procedure in your private setup note.

**Next:** [Check hardware readiness](readiness.md) with the installer and operator.
