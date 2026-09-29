# Source validation — 29 September 2026

## Result

Rechecked the handbook against accessible original documents, supplied photographs, the original platform PDF, and current public references. Three source-based improvements were made. A subsequent successful workstation connection revealed a scene-camera model discrepancy; the owner authorized correcting it to the installed D415 model. This is not a complete verification of all remote copies or the delivered hardware.

### Changes made

1. **VLA scene-camera mounting:** the linked [CAMVATE C-clamp](https://www.amazon.com/dp/B0BYDH27WQ) supplies threaded attachment points, not a ball head. The equipment list and selection notes now distinguish the clamp/adapters from the articulated stand and adjustable camera head. The sources page uses the same distinction.
2. **VLA scene-camera model:** updated all VLA setup references and photo labels to three D415 cameras, based on live USB enumeration and owner approval. Added the [official D415 product reference](https://www.realsenseai.com/products/stereo-depth-camera-d415/). The two wrist cameras remain D405.
3. **Optional TurtleBot tracking:** the original OptiTrack guide requires checking coordinate conventions. The software and readiness pages now ask the operator to verify axes and ground-plane origin, as well as receiving live poses. Current [OptiTrack streaming documentation](https://docs.optitrack.com/motive/data-streaming) also discusses coordinate conventions; the handbook does not prescribe an unverified setting for the existing VRPN installation.

## Original materials checked

| Material | Fresh comparison and conclusion |
|---|---|
| Supplied xArm photograph, IMG_1404.JPEG | Two arms, three scene-camera positions and two wrist-camera positions agree with the handbook. The earlier D435 scene identification was superseded by live workstation USB enumeration and owner approval: three D415 scene cameras and two D405 wrist cameras. A photograph alone does not establish every model. |
| Supplied ABC photograph, IMG_1401.JPEG | Two follower arms, two wrist cameras and one overhead camera agree. Leader arms, computer and stop controls are not all visible, so their presence is not inferred from this image. |
| Original platform.pdf | Compared the rendered original with the Go2 illustration. Go2, D1, front camera and wrist camera agree. The published PDF is byte-identical to the supplied original. EDU Plus and wrist D435 identification also use the owner's confirmation. |
| VLA system overview photograph | Two arm stands, control boxes, stop controls and headsets agree with the inventory. |
| Photo label assets | Camera model/count labels agree across VLA, ABC and Go2. No numbered label prefixes or task-tray callout were found. |
| Published camera-mount STL | Parsed its 6,472 triangles; native-coordinate bounds are approximately 17 × 25 × 62.46, consistent with the stated approximate dimensions if interpreted as millimetres. Material, print tolerances and physical fit were not tested. |
| Google Doc: Getting started with Turtlebots | Fresh export confirms Burger and the existing Ubuntu 20.04/ROS 2 Foxy environment. Its Humble installation links conflict with its stated environment; the handbook correctly uses the Foxy instructions instead. Private access information and research launchers remain excluded. |
| Google Doc: Setup teleoperation | Fresh export confirms Quest USB/ADB setup. The handbook correctly treats device detection as a basic connectivity check, not proof of working teleoperation. Research environments, port-forwarded applications and private paths remain outside scope. |
| Google Doc: Using the xArm 7 | Fresh export supports gripper installation with power off and wired network setup. The handbook defers power-on and stop recovery to the current UFACTORY procedure. |
| Google Doc: Using Teleoperation | Fresh export confirms the USB/ADB foundation. Project-specific runtime dependencies and research operation are intentionally not copied into the basic setup manual. |
| Archived Real-sense Camera Setup.docx | Read the original preview: D405 identification, standard 7–50 cm working range and SDK/Viewer setup agree. Historical VM/macOS issues and automatic firmware-update advice are not treated as universal current requirements. |
| Archived (Documentation) Optitrack Setup.docx | Read the original preview: calibration, ground-plane setup, rigid-body identity and VRPN streaming support the optional tracking section. Its coordinate-frame warning motivated the new readiness check. |
| Archived (Documentation) ROS1_2 bridge.docx | Read the original preview. Supports the legacy ROS 1-to-ROS 2 bridge concept, but its older distribution-specific commands are not suitable defaults for the handbook's current environments. |
| Archived Connecting to TurtleBots.docx | Read the original preview. Robot identity and matching environments agree. Credentials, private addresses and custom research bringup commands remain excluded. |
| Archived (Documentation)ROS2 Turtlebot3 Setup.odt | Read the original preview. Pi/OpenCR setup and matching ROS domain support the basic setup guidance. Research sensors, experiments and custom launchers remain excluded. |

The original shared folders were used as evidence only; no Dropbox folder link or private access details were added to the website. Unrelated research files and media were not treated as handbook setup sources.

## Public reference comparison

- **UFACTORY:** hardware installation, control-box connections and Studio network access agree with the current manufacturer instructions. The camera-stand listing explicitly names D435; its use with D405 is an owner-confirmed fit, not a claim made by that listing.
- **Unitree:** the current Payload article supports the D1 rail installation and front D435i mounting/connection guidance. Go2 EDU Plus is the owner-confirmed delivered version; generic Go2 marketing does not independently prove the lab's purchased configuration. The linked gantry listing is for Go2 EDU.
- **I2RT / ABC:** current assembly and hardware references support two followers, two leaders, four CAN interfaces and three D405 cameras. Box contents and a complete research kit are not assumed to be identical. The official software guide recommends Ubuntu 22.04; compatibility with the shared desktop's other environment is not asserted without testing.
- **RealSense:** camera models, ordinary working ranges, Viewer checks, Linux package guidance and separate Jetson instructions agree with current sources. Kernel and firmware compatibility still depend on the actual installed system.
- **Desktop / Quest:** NVIDIA's 96 GB Workstation Edition and Blackwell open-kernel-module requirements agree. Android USB permissions/ADB and Meta developer setup match the basic connectivity instructions.
- **TurtleBot / ROS / OptiTrack:** Burger equipment and the existing Foxy/Focal pairing agree with ROBOTIS and ROS documentation. Foxy's end-of-life status is disclosed. The legacy ROS bridge is scoped to the existing tracking installation rather than presented as a universal VRPN requirement.
- **Accessories:** current linked product descriptions were checked against the named items. The CAMVATE clamp/head mismatch was corrected. Product listings do not prove purchase quantities or physical fit.

All **77 original published external URLs** were requested again. Direct results were 73 HTTP 200, one timeout, two HTTP 403 and one HTTP 567; none returned 404. The four exceptions were followed up through web browsing or the browser. A successful response is not proof of compatibility, stock, or purchased contents. The added D415 product page was subsequently checked and returned HTTP 200, bringing the published total to 78 distinct external URLs. The full per-link record is in [the link audit](2026-09-29-links.md).

## Remaining verification limits

- Earlier attempts to both remote desktops timed out, but a follow-up connection to `naliseas-workstation` succeeded. Its current `robocoop` setup document and relevant camera source files were read; `robocoop` itself is a workspace without a top-level Git repository. Research execution remains outside the handbook's scope.
- A clean `unidog_nav` checkout is also present on the reachable workstation, at commit `785362ec1886a4b31ae857ce46923d67d1433824`. Its README confirms the workstation/onboard split and built-in camera path. This does not establish that the separate copy on `naliseas` is identical. Direct attempts to `naliseas`, including a longer timeout, and an attempt through the reachable workstation still failed.
- Follow-up after the owner requested another retry: the workstation resolves `naliseas.local` to the configured destination and accepts a TCP connection to its SSH port. Both SSH ProxyJump and nested SSH using existing workstation credentials time out during the server greeting, including a 45-second attempt. No authentication or robot commands were reached on that host. The local direct route uses a VPN interface and still times out; the evidence does not establish the underlying server/network cause. The working connection command or address was requested from the owner. No network or SSH settings were changed.
- The lab teleoperation checkout is at `63f7fd68131864291319e3a18cec7f8162da9ff4`, with local changes. Its TeleImager submodule is at `fdc1ae415aa885d8904780191745e2d053b4f23e`, also modified. The current working configuration, rather than upstream template defaults, was examined. It configures two wrist views and three scene views; some scene-camera comments name D415.
- **Scene-camera discrepancy:** read-only USB enumeration on the workstation reports **three Intel RealSense D415 devices (8086:0ad3)** and **two D405 devices (8086:0b5b)**. This supports the five-camera count and D405 wrist identification, but conflicts with the handbook's D435 scene-camera identification from an earlier owner confirmation. No streams or robot commands were started. The owner authorized the correction. VLA inventory, overview, captions, SVG photo labels, connection map, software/readiness checks, shared camera summary and product references now use D415. The D435 wording in the UFACTORY wrist-mount listing and the Go2 D435/D435i identification are unchanged.
- [Vention design 506323](https://vention.com/machine-builder/506323) and the original shared-design invitation both resolve to sign-up in the current browser session. Its private CAD geometry and bill of materials could not be inspected. The handbook already identifies this access requirement.
- The original purchase-order export was not available for a fresh recount. Accessory descriptions were checked against current listings; recorded purchase quantities were not independently re-established.
- Items outside the photographs, received kit contents, mount fit, cable reach, power/network assignment and physical operation need the delivered equipment. No robot, camera, driver installation or motion procedure was executed in this review.

## Site checks after corrections

- Strict MkDocs build passed.
- All 26 generated content pages passed internal-link/fragment and navigation checks.
- All 72 hardware-table rows passed the associated-link check.
- All 16 shell examples passed syntax checks; this is not execution or compatibility testing.
- Privacy and obsolete-content checks passed. The only image-asset change is the approved D435-to-D415 text replacement in the existing VLA SVG; the underlying photograph is unchanged.
- The new VLA mounting text and TurtleBot tracking text were checked in the local rendered preview.
- `git diff --check` passed.

The changes are local and uncommitted. This report complements the earlier visual/editorial review; it does not claim that the live GitHub Pages site already contains these changes.
