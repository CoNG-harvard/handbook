# ABC Box hardware

**Goal:** identify one complete station before installing software. Use the delivered packing list to confirm inclusion; a camera mount is not a camera.

<figure class="handbook-figure" markdown="1">

![Labeled ABC Box station: 1, both robot arms; 2, two wrist cameras; 3, overhead camera; 4, camera frame.](assets/abc-box-station-labeled.svg){ loading=lazy width=1000 height=750 }

<figcaption markdown="1">

**1** Both robot arms · **2** Two wrist cameras · **3** Overhead camera · **4** Camera frame.

Lab photograph provided in September 2026. The leaders, computer, and stop control are not identified in this view.

[View full-size image](assets/abc-box-station-labeled.svg) · [Source photograph](assets/abc-box-station.jpg)
{ .figure-links }

</figcaption>

</figure>

## 1. Check the ABC Box package

I2RT lists these items for the full ABC Box. Confirm the order specifies **ABC Box**, rather than the Research Kit. [Manufacturer package list](https://i2rt.com/products/abc-box)

| Listed equipment | Quantity |
|---|---|
| Follower arm with mounting hardware | 2 |
| Small PC: AMD R7-8745HS, 16 GB RAM, 1 TB SSD | 1 |
| Integrated touchscreen | 1 |
| D405 camera mount positions | 3: two wrist, one overhead |
| Control cable, quick-start guide, and configuration files | 1 package |

The product describes a hardware emergency stop. Ask the supplier to demonstrate which equipment it cuts off, and the procedure for restarting afterward.

## 2. Confirm the additional equipment

| Equipment needed for this workflow | Quantity |
|---|---|
| Compatible leader arms and handles | 2 |
| RealSense D405 cameras | 3 |
| Camera USB data cables | 3 |
| Working communication connection for each follower and leader | 4 channels |
| Matching grippers, power supplies, and mains leads | Confirm the complete supplied set |
| Stable work surface, cable restraints, and lighting | 1 station |
| Task objects and backup storage | As needed |

**Leaders and cameras:** their inclusion is not explicit in the ABC Box package list. Get written confirmation before ordering extras. The [ABC assembly guide](https://abc.bot/hardware.html) uses two wrist D405s and one overhead D405. Follow the delivered Box's assembly instructions rather than buying all parts from that separate, build-your-own station list.

**Leader choice matters:** the collection application's example configuration uses passive GELLO leaders, which measure joint position without driving motors. Powered YAM leaders use different drivers and configuration. Record the actual leader and gripper models; do not copy example settings blindly. [I2RT hardware configuration](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md)

**Communication:** CAN is the control connection used by this software. Have the supplier identify each supplied interface before purchasing adapters; do not assume all four require an additional external adapter.

## 3. Connect and label the station

1. Have the installer secure the follower and leader mounts using the supplied instructions.
2. Label left/right followers, their paired leaders, and each control cable.
3. Mount and label the top, left-wrist, and right-wrist cameras; connect them to the recording computer.
4. Route power and data cables clear of joints and the work area.
5. Record device identities, approved resting poses, and the stop procedure in your private setup note.

**Next:** [Install and rehearse](install.md) before enabling real teleoperation.
