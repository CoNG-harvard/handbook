---
hide:
  - footer
---

# ABC Box basic software

**Goal:** identify the control computer, confirm that Linux detects its arm interfaces, and display the three cameras. Complete [equipment and connections](hardware.md) first. Keep the arms stationary and leave leader/follower control disabled.

## 1. Use the delivered configuration

Ask the supplier to identify the installed software, its version, and which checks run on the **Box PC** and which run on the **shared workstation**. Preserve the delivered configuration and calibration.

**Preconfigured system:** use the supplier's installed environment and connection check. Skip SDK installation if the supplied system already works.

**New I2RT SDK installation:** follow its [software setup guide](https://doc.i2rt.com/getting-started/sw-setup) for the supplier-approved revision. It recommends Ubuntu 22.04 and Python 3.11; this does not establish compatibility with the shared Ubuntu 24.04 workstation. The guide covers Git, uv, build dependencies, and a separate Python environment. Install on the host selected for the delivered arm and leader models.

For an I2RT SDK installation, open its repository folder in Terminal and activate the environment created by the vendor guide:

```bash
source .venv/bin/activate
python -c "import sys; print(sys.executable)"
```

**Expected:** a Python path inside this repository's `.venv`. Then check that Python can find the package without connecting to an arm:

```bash
python -c "import i2rt; print('I2RT package available')"
```

**Expected:** `I2RT package available`. This confirms that Python can find the package; it does not test every dependency or motor communication. If the supplied application uses a different environment, use the supplier's check instead.

## 2. Identify the arm interfaces

On the computer with the USB-CAN adapters, run:

```bash
ip -details link show type can
```

**Expected:** the CAN interfaces specified in the supplier's connection plan. No output means Linux currently lists no CAN interfaces on this computer. The [referenced ABC configuration](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md) uses four CAN channels, including its passive GELLO leaders. Match each channel to its physical arm and label; the delivered configuration determines the adapter count. The supplier configures the bitrate and persistent names following [I2RT's CAN setup](https://doc.i2rt.com/getting-started/sw-setup). A listed interface does not confirm motor communication.

Powered YAM leaders and passive GELLO leaders need different setup. Do not assume the [four-CAN YAM Cell example](https://doc.i2rt.com/products/yam-cell) matches every ABC Box package. Resolve the delivered leader type before using its control examples.

## 3. Check the three cameras

On each camera's connected host, follow the [RealSense Viewer check](../getting-started/software.md#3-install-realsense-viewer). Identify the **left wrist**, **right wrist**, and **overhead** D405 views by serial. Check them together on the agreed host arrangement, then close Viewer. For the overhead view, check color coverage at the installed height; only require useful depth if the session needs it. The D405's [standard ideal depth range is 7–50 cm](https://www.realsenseai.com/product-family/d405-series/).

**Ready when:** the software and interface assignments are recorded and all three views are stable. Calibration, motor checks, and enabling a leader/follower pair remain part of the supplier-led handover.

**Next:** [Hardware readiness](readiness.md).
