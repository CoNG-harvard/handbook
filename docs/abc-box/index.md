# ABC Box

ABC Box is a two-arm teleoperation station from I2RT. You move a pair of **leader arms** by hand; the **follower arms** perform the task. The recording combines camera views and arm movements into a demonstration for later learning.

**Your first goal:** rehearse the recording controls in software, then save and review one short demonstration on the commissioned station.

!!! note "Station photograph pending"
    Add a real photograph of the delivered station, showing its leaders, followers, cameras, and physical stop. For the manufacturer's product images, see [I2RT ABC Box](https://i2rt.com/products/abc-box).

## Setup guide

| Step | Guide | You are finished when… |
|---|---|---|
| 1 | [Hardware and connections](hardware.md) | The delivered package and additional equipment are identified |
| 2 | [Install and rehearse](install.md) | The mock interface saves a pretend demonstration |
| 3 | [Configure and record](operation.md) | A supervised real episode is saved and reviewed |

This guide uses I2RT's [YAM-ABC-Reproduce](https://github.com/i2rt-robotics/yam-abc-reproduce) collection application. Confirm the software revision and leader type with the supplier before applying it to the delivered ABC Box. The lab has not yet validated an ABC Box installation.

## Which computer does what?

The **full ABC Box** includes a small recording computer and touchscreen. I2RT says basic demonstration collection does not require another host. The similarly named **ABC Research Kit** has a different package list; confirm which variant you are receiving. [Product package details](https://i2rt.com/products/abc-box)

The shared **RTX PRO 6000 workstation** can be reserved for later model work. Keep its existing project environments separate. ABC training and policy execution are outside this first recording guide; they require their own environment and validation on the selected GPU.

Before installing, read [the basic command conventions](../getting-started/index.md#4-read-command-blocks-correctly) and choose `<ABC_DIR>` using the [folder guide](../getting-started/paths.md). You do not need to install the xArm or Go2 software for this project.

## Sources and verification

The [reference page](reference.md) records the official guides and source revision used here. The instructions were checked against source; no ABC hardware was operated during this documentation update.
