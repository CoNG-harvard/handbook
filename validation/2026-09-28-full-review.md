# Whole-site review — 28 September 2026

Reviewed all 26 published content pages against commit `f8245dd`, the original supplied materials available locally, current manufacturer documentation, and the recorded owner corrections. This report stays outside the published website.

## Assessment

The handbook is a coherent preparation and supervised setup manual. Equipment models and visible counts agree with the supplied photographs and owner corrections. It is not yet an independently reproduced, end-to-end hardware installation: station-specific wiring, configuration, and physical acceptance still require the owner or installer. No robot was operated and no software was installed on robot or workstation hardware during this review.

## Findings corrected

| Finding | Correction |
|---|---|
| Mobile navigation opened inside the current project, hiding the handbook-wide outline behind a back arrow | Keep all project sections in one scrollable drawer; retain the current page's table of contents as an inline expansion |
| The shared computer page counted only two ABC arm interfaces, contradicting the referenced four-channel setup | Specify two follower and two leader CAN channels; distinguish channels from external adapter count. The software page now explicitly notes that the referenced passive GELLO leaders also use CAN |
| ABC power supplies and the camera support frame appeared as guaranteed Box package contents, although the product's explicit list does not establish that | Keep advertised mount kit, followers, computer/display, and control cable in the package section. Account for the frame and matching power supplies separately, checking the delivered packing list before purchasing |
| The D1 setup sequence required calibration and powered acceptance before basic software was checked | Keep mounting and cable inspection on the D1 page; place calibration, gripper/joint checks, and stop acceptance after software on hardware readiness |
| Go2's connection map continued to label the D1 arm connection as unresolved even though Unitree documents it | Clarify that the pending item is the added wrist-camera USB host and route, not whether the supported D1 mounting exists |
| The generic camera check required depth everywhere, including the overhead D405 view | Check color plus required depth at the intended working distance. State the D405's standard 7–50 cm ideal depth range and distinguish overhead color coverage from required depth |
| The VLA guide assumed the supplied 2 m camera cable necessarily reached the host | Retain the included cable, but check route and movement slack before choosing a replacement or extension |
| ABC readiness assumed one receiving computer despite the still-unconfirmed split between Box PC and workstation | Check simultaneous views on the agreed hosts |
| TurtleBot3's fresh-computer SSH check omitted the client prerequisite | Add the Ubuntu OpenSSH client check/install route and explicit placeholder replacement |
| A few unresolved equipment details were not in the central open-items list | Include the work-table rating, tray model, and ABC power set; link the unresolved workstation build row to that list. Give TurtleBot3 the same overview pointer to open items as the other projects |

No camera models, inventory photographs, image labels, user-selected mounts, or research scope were changed.

## Original-resource comparison

| Resource | What was checked | Result and limit |
|---|---|---|
| Supplied xArm photographs, including the earlier full-station view | Arms, stands/control boxes, cameras, headsets, and label targets | Two arms; two wrist positions; three scene cameras; earlier view shows two headsets and two control boxes. D405/D435 model assignments follow the owner's corrections. Camera model text and absence of task-tray callouts are consistent across SVGs and pages |
| Supplied ABC photograph | Follower count, two wrist cameras, overhead camera, frame, and base interfaces | Two followers and three camera positions match the guide. The image does not establish leader model, package variant, power ratings, or stop behavior |
| Supplied Go2 platform image/PDF and owner corrections | Go2/D1, D435i front and D435 wrist, included onboard computer | Consistent. EDU Plus and camera/mount selections are owner-provided facts; no separate Orin purchase restored |
| Saved RoboCoop and teleoperation repository files | Two-arm/headset configuration and camera roles | Cached bimanual configuration supports a single headset controlling two arms. Runtime camera selection is not treated as the full physical inventory. Research launchers and private machine details remain excluded |
| Saved UniDog README and earlier source records | Workstation/onboard separation and camera-access distinction | The source uses the built-in camera in some flows; the guide correctly distinguishes it from the added D435i. Research server commands remain excluded |
| Original Google document, “Getting started with Turtlebots,” exported earlier in this session | Burger, Ubuntu 20.04/Foxy, conflicting Humble links, optional Motive/OptiTrack and bridge | All present in the original export. The guide preserves the legacy distinction and does not reproduce credentials, private addresses, custom launchers, or a false claim that VRPN is ROS 1-only |
| User-supplied Amazon order history and later confirmations | Accessory models, camera clamps, gripper STL, Vention stand link | Retained the previously recorded owner selections. The order export was not newly retrieved; this review does not claim to have re-counted the physical consumables or accessed the private Vention design |

Fresh read-only SSH attempts to both `naliseas` and `naliseas-workstation` timed out. The repository comparison is against saved source copies, not a verification of the latest remote revisions.

## Manufacturer checks

- [UFACTORY hardware installation](https://docs.xarm.ufactory.cc/2.hardware_installation.html) and [Studio connection](https://docs.ufactory.cc/user_manual/ufactoryStudio/3.connection.html): independent arm/control-box pairing, wired network arrangement, AC-disconnect requirement, and browser port 18333 agree with the guide.
- [UFACTORY camera stand](https://www.ufactory.us/product/ufactory-xarm-camera-stand): D435 listing and included 2 m USB-C cable verified. D405 fit remains the owner's confirmation, not a vendor-listed specification.
- [Unitree payload installation](https://support.unitree.com/home/en/developer/Payload): loaded in the browser after automated retrieval failed. Verified square rail nuts, M4 × 10 screws, and documented arm power/Ethernet connection. The official D435i mounting procedure is also present. The guide avoids inferring a pinout from inconsistent interface wording in the source.
- [I2RT ABC Box](https://i2rt.com/products/abc-box), [hardware repository](https://github.com/i2rt-robotics/yam-abc-reproduce/blob/main/docs/hardware.md), and [ABC assembly](https://abc.bot/hardware.html): package distinction, camera layout, built-in follower interfaces, and four-channel leader/follower arrangement checked. Delivered configuration is still to verify.
- [I2RT software setup](https://doc.i2rt.com/getting-started/sw-setup): browser confirms Ubuntu 22.04 recommended, Python 3.11 recommended, virtual environment, SDK import, and CAN setup. The guide does not claim this validates Ubuntu 24.04 compatibility.
- [RealSense Linux packages](https://github.com/realsenseai/librealsense/blob/master/doc/distribution_linux.md), [D405 stream guidance](https://github.com/realsenseai/librealsense/discussions/11689), and [D405 specifications](https://www.realsenseai.com/product-family/d405-series/): utilities/permission packages, kernel caveat, matching D405 stream settings, and close-range depth checked. D435 and D435i product links remain distinct.
- [NVIDIA RTX PRO 6000 family](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/) and [open kernel modules](https://download.nvidia.com/XFree86/Linux-x86_64/610.43.02/README/kernel_open.html): 96 GB Workstation Edition and Blackwell's open-module requirement agree with the guide.
- [Android device setup](https://developer.android.com/studio/run/device) and [Meta device setup](https://developers.meta.com/horizon/documentation/native/android/mobile-device-setup/): Ubuntu rules/group membership, developer setup, and USB authorization checked. No teleoperation application is implied by an ADB connection.
- [ROBOTIS bringup](https://emanual.robotis.com/docs/en/platform/turtlebot3/bringup/), [ROS support schedule](https://www.ros.org/reps/rep-2000.html), and [OptiTrack streaming](https://docs.optitrack.com/motive/data-streaming): network/ROS compatibility, Foxy lifecycle, and optional rigid-body streaming agree with the guide. The ROBOTIS legacy site advertises a migration; its present links are still reachable.

## Website and link checks

- Strict MkDocs build: passed after corrections.
- 26 content pages: no missing local page, asset, or anchor targets.
- 72 hardware/specification rows: each has a product, catalog, assembly, or clearly marked unresolved-build reference. A generic catalog or open-items link is not a confirmed part selection.
- 16 Bash blocks: syntax parsed after replacing documented placeholders; none were run against hardware.
- All 26 pages rendered at desktop width and at 390 px mobile width: one page title, shared navigation present, no document-level horizontal overflow. Tables intentionally scroll within their own area on mobile. Full mobile drawer and cross-project navigation verified after the CSS correction.
- Published image assets remain byte-identical to the committed versions; supplied images and vector callouts were inspected.
- Public Markdown and generated search index: no Dropbox/source-folder links, research launchers, remote-host names, literal private LAN addresses, or user home-directory paths.
- External audit: 77 distinct URLs; 73 returned HTTP 200, with no 404. Four command-line checks failed: Unitree payload (567), AMD (timeout), Kingston and RobotShop (403). Unitree was then read in the browser; the other three were retrieved with web browsing. Some evidence comes from web retrieval rather than a successful direct HTTP request.
- Vention returned a sign-up page: access restriction is correctly disclosed. Its design and bill of materials were not inspected. HTTP 200 alone does not verify a product's suitability or purchased variant.
- `git diff --check`: passed.

## Remaining limits

The centralized open-items list remains the place for delivered package variants, exact cable routes, unspecified hardware revisions, calibration, and physical stop/clearance acceptance. TurtleBot3 also needs a station photo and confirmation of its current operator environment. These cannot be established by photographs and web documentation alone.

No commit, push, or deployment was performed during this review.
