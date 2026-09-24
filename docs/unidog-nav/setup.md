# Install the project software

**Run on the Linux GPU workstation shared with VLA Pipeline.** Finish [computer preparation](../getting-started/computer.md) first. Keep the physical robot out of this initial software test.

## 1. Download the workstation repository

Using your authorized GitHub account:

```bash
cd ~
git clone --recurse-submodules https://github.com/CoNG-harvard/unidog_nav.git
cd ~/unidog_nav
git submodule status
```

**Expected:** `repos/NaVILA` appears. A submodule is another repository used inside the main one. If it was not downloaded:

```bash
git submodule update --init --recursive
```

The inspected lab checkout includes uncommitted changes. A new clone retrieves committed code only. Ask for the [dated source handoff](../getting-started/sources.md#dog-platform-files) before assuming every recent feature is available.

## 2. Run a mock bridge with no robot

A mock bridge uses stored images and pretend actions. Use port **18766** for this test so it cannot be mistaken for the normal robot tunnel on 8766.

**Terminal A:**

```bash
cd ~/unidog_nav
python3 robot/primitive_server.py --mock --port 18766 \
  --mock-frames test_frames/real_front_wall1
```

This uses Python's standard library; a GPU model is not needed. If that image folder is absent from your handoff, obtain a sample JPEG folder and use its path after `--mock-frames`.

**Terminal B:**

```bash
cd ~/unidog_nav
python3 scripts/robot_client.py --url http://127.0.0.1:18766 health
python3 scripts/robot_client.py --url http://127.0.0.1:18766 image /tmp/unidog-mock.jpg
```

**Expected:** health reports `"ok": true`, `"backend": "mock"`, and `"real": false`; the second command saves an image. Open `/tmp/unidog-mock.jpg` in the workstation's image viewer. It should show a saved scene, not a live feed.

Stop Terminal A with **Ctrl+C** when finished. Success here checks the client/bridge connection only.

## Installation checkpoint

You can run the mock client and view a saved image. **Next: [connect the real robot and check its camera](robot-bridge.md).** No model installation is required for that step.

## Optional model setup {#3-choose-which-model-you-need}

Install a model later, when you need language/image planning or saved-image evaluation. Both paths require validation on the selected RTX PRO 6000.

- <span id="qwen-installation-and-check"></span>[Qwen installation and check](models.md#qwen-installation-and-check)
- <span id="navila-installation-and-saved-image-check"></span>[NaVILA installation and saved-image check](models.md#navila-installation-and-saved-image-check)
