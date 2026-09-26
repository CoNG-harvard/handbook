---
hide:
  - footer
---

# Hardware troubleshooting

Use these checks with the installer while the equipment is stationary. Record the affected device and what changed. Follow the delivered equipment's shutdown procedure before changing robot power or control connections.

| What you notice | First physical check | Continue when… |
|---|---|---|
| A camera view is missing | Match its serial and cable label; check the data cable and assigned USB port. Have the installer compare the camera alone with all required views together. | Every required view remains available together |
| A camera shows the wrong area | Match the live view to the physical camera; inspect its mounting angle and obstructions. Record any mount change and have the installer review calibration. | The intended gripper or work area is visible |
| A wrist cable becomes tight | Stop the check and have the installer review slack and attachment points through the approved movement range. | The cable avoids joints, snag points, and strain at the connector |
| An arm and controller do not match the labels | Compare serials, rig A/B labels, and the supplied cable set with the packing list. Do not enable movement to identify an arm. | Each arm has an identified matching control box or interface |
| A mount or stand moves | Have the installer check the approved drawing, fasteners, and supporting surface. | The installer approves the corrected attachment |
| An ABC leader/follower pairing is unclear | Compare the left/right labels and interface record with the supplier's connection plan. | Both pairs are identified before calibration or movement |

For a D405, also check working distance when the depth view is poor: RealSense gives a standard ideal range of **7–50 cm**. This applies to the D405, not automatically to a D435 or D435i. [D405 specifications](https://www.realsenseai.com/product-family/d405-series/)

For xArm cable changes, UFACTORY requires external AC to be disconnected before plugging or unplugging arm cables. The delivered model's installation instructions take precedence. [UFACTORY hardware installation](https://docs.xarm.ufactory.cc/2.hardware_installation.html)

If the connection, mount, or power arrangement is undocumented, obtain the missing instructions from the owner or supplier before changing it. Add the issue to the [station record](station-record.md).

**Return to readiness:** [VLA Pipeline](../vla-pipeline/readiness.md) · [Self Improvement Learning](../unidog-nav/readiness.md) · [ABC Box](../abc-box/readiness.md).
