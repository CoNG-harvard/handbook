---
hide:
  - footer
---

# Hardware troubleshooting

Use these checks with the installer while the equipment is stationary. Follow the equipment's shutdown procedure before changing robot power or control connections, and record what changed.

| What you notice | First physical check | Continue when |
|---|---|---|
| A camera view is missing | Match its serial and cable label; check the data cable and USB port. Compare the camera alone with all required views together. | Every required view is available together |
| A camera shows the wrong area | Match the live view to the physical camera; check its angle and obstructions. Record any mount change and have the installer review calibration. | The intended gripper or work area is visible |
| A wrist cable becomes tight | Stop and have the installer review slack and attachment points through the approved movement range. | The cable avoids joints, snag points, and strain at the connector |
| An arm and its control box do not match the labels | Compare serials, rig labels, and the supplied cable set with the packing list. Do not enable movement to identify an arm. | Each arm has an identified matching control box or interface |
| A mount or stand moves | Have the installer check the drawing, fasteners, and supporting surface. | The installer approves the corrected attachment |
| An ABC leader/follower pairing is unclear | Compare the left/right labels and interface record with the supplier's connection plan. | Both pairs are identified before calibration or movement |

**D405 depth is poor:** check the working distance. RealSense specifies an ideal range of **7–50 cm** for the D405; this does not apply to the D435 or D435i. [D405 specifications](https://www.realsenseai.com/product-family/d405-series/)

**xArm cable changes:** disconnect external AC first, as UFACTORY requires. [UFACTORY hardware installation](https://docs.xarm.ufactory.cc/2.hardware_installation.html)

If a connection, mount, or power arrangement is undocumented, get the missing instructions from the owner or supplier before changing it, and add the issue to the setup notes.

## Software connection checks

| What you notice | Check |
|---|---|
| `nvidia-smi` fails | Return to the [GPU driver check](software.md#2-check-the-nvidia-driver); ask the installer to check the driver and restart requirement |
| Viewer cannot find a camera | Close other camera applications, check its USB data connection, and review device permissions and kernel support in the [installation guide](software.md#3-install-realsense-viewer) |
| xArm Studio does not open | Check that the correct control-box address and port `18333` are used and the workstation is on the same network range |
| Quest reports `unauthorized` | Put on the headset and approve USB debugging for this workstation; see [Quest connection checks](../vla-pipeline/software.md#3-check-quest-usb-connections) |
| Quest reports `no permissions` | Check the Ubuntu USB rules and `plugdev` membership, then log out and back in after a group change; see [Quest connection checks](../vla-pipeline/software.md#3-check-quest-usb-connections) |
| Onboard-computer SSH fails | Check the agreed address and network for a timeout, or the authorized login/key for `Permission denied`; see [onboard-computer access](../unidog-nav/software.md#2-check-onboard-computer-access) |
| ABC Box has missing interfaces | Check the computer receiving the adapters and the supplier's interface plan; see [ABC software](../abc-box/software.md#2-identify-the-arm-interfaces) |

**Return to readiness:** [VLA Pipeline](../vla-pipeline/readiness.md) · [Self Improvement Learning](../unidog-nav/readiness.md) · [ABC Box](../abc-box/readiness.md)
