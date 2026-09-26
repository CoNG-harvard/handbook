# Lab resources

The [Robotics Lab Dropbox folder](https://www.dropbox.com/scl/fo/f30n7ry2f82y572bja84k/h?rlkey=nnz9kh52et3ri2mdt5xbkbg0l&dl=0) contains earlier setup notes, experiment videos, and purchasing records. Use it for background alongside your project's current setup guide.

Open the shared folder, then follow the folder and file names below. Preview individual files before downloading; the full archive includes large video collections. If Dropbox returns you to the folder's home page, navigate through its folders again.

## Find the relevant material

| Where to look in Dropbox | What you will find | How to use it |
|---|---|---|
| `Documentations` → `Real-sense Camera Setup.docx` | D405 camera notes, Viewer screenshots, Python examples, and past installation attempts | Start with the camera check below; use current SDK instructions for installation |
| `Documentations` → `robotic arms` | `UR5e Programming with Python ROS1.docx` and `ur_simulator.md` | Background for Universal Robots equipment; these are not the xArm or ABC Box setup instructions |
| `Documentations` → `ROS2 How-to` | A folder of ROS2 reference material | Consult when a specific task requires ROS2; it is not an extra prerequisite for the handbook's first recording |
| `PushT` | Video files and experiment folders such as `baseline`, `new shape`, `random_goal`, and `real_exps` | Ask the experiment owner which recordings illustrate your task; these are not a verified training-data release |
| `quadrupeds` | Video files including `ICRA25_3740_VI_i.mp4` and `iros_submission.mp4` | Historical experiment references; confirm the robot and software used before comparing with Self Improvement Learning |
| `Research Computing` → `masked world model on fasrc.odt` | An older environment note for a masked world model on the research cluster | Background for that experiment, not the shared RTX PRO 6000 installation recipe |
| Folder root → `Items to buy.xlsx` and `Addtional items to buy.xlsx` | Purchasing spreadsheets dated January 2023 in Dropbox | Historical purchasing records; use the handbook's [current hardware lists](hardware.md) for the new setup |

Filenames above retain the archive's spelling so you can find them. The folder also contains drone, ultrasound, paper, and photo/video collections beyond the three current project guides.

## Check a RealSense camera before recording

The lab's **Real-sense Camera Setup** note identifies the D405 and illustrates a basic check: connect the camera, open RealSense Viewer, and enable a stream to see an image. This is useful when preparing the D405 cameras used by VLA Pipeline and ABC Box.

**Run on the computer connected to the camera.** For xArm recording, that is the shared workstation; for ABC Box, it is the station's recording computer. Have the installer provide the SDK version approved for that station, following the [official Linux installation guide](https://github.com/realsenseai/librealsense/blob/master/doc/distribution_linux.md). Preserve a supplier-configured ABC image until its setup has been reviewed.

1. Close other programs using the camera and connect one camera with its USB data cable.
2. Open Terminal and run:

    ```bash
    realsense-viewer
    ```

3. Select the camera and enable a supported stream. Check that the image changes when you move an object in view; record the device serial and its intended position.
4. Stop streaming and close Viewer before starting the project's camera or recording service. Repeat for the other cameras.

**Expected:** the camera is detected and produces a live image. If `realsense-viewer` is missing, ask the installer to check the SDK tools. If the camera is missing, check its cable, USB port, permissions, and whether another program has it open. The [official Viewer guide](https://github.com/realsenseai/librealsense/blob/master/tools/realsense-viewer/readme.md) describes its controls.

This check establishes camera connectivity, not calibration or correct recording settings. Continue with [xArm camera configuration](../vla-pipeline/teleop/setup.md) or [ABC camera identities](../abc-box/operation.md#2-identify-the-cameras). For the dog's D435i and onboard computer, follow [robot bridge preparation](../unidog-nav/robot-bridge.md).

## How to interpret the older notes

- **Camera software:** the 2023 note includes older Python examples and unsuccessful Mac/virtual-machine attempts. Treat those as historical observations, not current compatibility guarantees. Have the installer review firmware changes against the station's approved SDK before applying them.
- **Model environments:** the research-computing note discusses Python 3.9, TensorFlow 2.6/2.8, and CUDA 11.2. Keep that experiment separate from the [RTX PRO 6000 setup](computer.md) and each project's model environment.
- **Robot instructions:** match every procedure to the robot model, control software, and source revision. A UR5e procedure does not configure an xArm; an old quadruped video does not establish Go2/D1 readiness.

## Review record

**Reviewed on 26 September 2026:** the full eight-page RealSense document preview and the one-page research-computing note, plus the relevant folder/file listings. The video contents, purchasing spreadsheet contents, ROS2 documents, and UR5e instructions were not validated in this review. No robot, camera, or archived installation commands were run.

The archive supplements the [source handoff](sources.md). It does not replace the approved source bundles, device configuration, or supervised acceptance checks required by the project guides.
