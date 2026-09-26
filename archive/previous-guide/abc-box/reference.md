# Reference and model handoff

## Official sources

- [ABC Box product and package list](https://i2rt.com/products/abc-box) — distinguish the full Box from the Research Kit and confirm the delivered accessories.
- [YAM-ABC-Reproduce](https://github.com/i2rt-robotics/yam-abc-reproduce) — the I2RT collection application used by this guide.
- [Hardware configuration](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md) and [Collect & Review](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/collect.md) — device naming, calibration, recording, and operator controls.
- [ABC assembly guide](https://abc.bot/hardware.html) — the separate build-your-own station, useful for understanding camera roles; not an ABC Box packing list.
- [ABC research code](https://github.com/amazon-far/abc) — the model, data, simulation, and deployment stack. This is a separate repository from the collection application.

## What was checked?

On **24 September 2026**, the product information and I2RT source at [`7d9f9d135a2b949de54a349856b65863f81319e1`](https://github.com/i2rt-robotics/yam-abc-reproduce/tree/7d9f9d135a2b949de54a349856b65863f81319e1) were reviewed. Checks covered the Python requirement, collection extras, submodule URL, GUI arguments, example station/camera files, and session controls.

Use that identifier for `<ABC_SOURCE_REVISION>` when reproducing this documentation, unless the supplier provides a different approved release. A newer release may change commands or configuration. `<ABC_DIR>` and `<ABC_DATA_DIR>` remain your own installation and recording locations.

This is a source-checked guide. The delivered hardware, camera bandwidth, calibration, recording performance, and clean installation still need an acceptance session. The software rehearsal described here was not executed during the handbook update.

## Before adding a trained model

First keep a verified real recording and its station configuration. Ask the model owner for the compatible checkpoint, source revision, camera views, action meaning, and approved evaluation procedure.

The shared RTX PRO 6000 can be used for a separately validated model environment. Do not reuse the VLA Pipeline environment merely because both projects mention openpi. The I2RT application has its own backend dependency groups, and changing its uv selection can replace installed dependencies. Follow the upstream [training guide](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/training.md) and [deployment guide](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/deploy.md) with the maintainer.

A remote model service also needs an agreed network connection to the recording/control computer. Record that design and coordinate GPU use through the [shared-workstation handover](../getting-started/hardware.md#using-the-shared-workstation). Hardware compatibility and successful collection alone do not validate a trained policy.
