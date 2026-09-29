---
hide:
  - footer
---

# TurtleBot3 equipment and connections

**Goal:** prepare one complete Burger robot and its network connection. Quantities below are **per robot**, not the lab's fleet size. Start with the delivered kit's packing list; internal parts are listed for identification, not as additional purchases.

## 1. Gather the equipment

| Equipment | Quantity | Product or reference |
|---|---|---|
| TurtleBot3 Burger chassis, drive wheels and motors, and caster | 1 robot; 2 drive wheels/motors and 1 caster | [ROBOTIS Burger parts list](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/#components) |
| Raspberry Pi onboard computer and microSD card | 1 each, included in the complete kit | [ROBOTIS specifications](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/#specifications) — identify the installed Pi revision |
| OpenCR control board | 1, included | [ROBOTIS parts list](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/#components) |
| LiDAR with its matching interface and cables | 1 set, included | [ROBOTIS sensor and kit reference](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/#components) — identify the installed LDS model |
| Robot battery and matching charger | 1 each | [ROBOTIS kit power components](https://emanual.robotis.com/docs/en/platform/turtlebot3/features/#components) |
| Internal power/data cables, power adapter, fasteners, and assembly tools | 1 kit set | [Burger assembly instructions](https://emanual.robotis.com/docs/en/platform/turtlebot3/hardware_setup/) |
| Operator computer | 1 available for the session | [ROBOTIS PC setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/) — match the robot's ROS version |
| Network with Wi-Fi for the robot | 1 shared network | [ROBOTIS network and bringup guidance](https://emanual.robotis.com/docs/en/platform/turtlebot3/bringup/) |

The standard Burger has no camera. Raspberry Pi and LiDAR revisions vary between kits; use the labels on the delivered robot when selecting instructions or replacement parts.

### Optional: OptiTrack tracking

Use this only when the session needs external position measurements. It is not required for basic robot connection or sensor checks.

| Equipment | Quantity | Product or reference |
|---|---|---|
| Installed, calibrated OptiTrack camera system and Motive computer | 1 room system, shared | [OptiTrack rigid-body tracking](https://docs.optitrack.com/motive/rigid-body-tracking) |
| Tracking markers and a secure robot attachment | 1 marker arrangement per tracked robot | [OptiTrack rigid-body setup](https://docs.optitrack.com/motive/rigid-body-tracking) |
| Network connection to the tracking computer | 1 connection per participating computer | [OptiTrack streaming guide](https://docs.optitrack.com/motive/data-streaming) |

Camera count, marker arrangement, and network equipment depend on the installed room system; this is not a shopping list for building a new motion-capture room.

## 2. Connection map

<div class="connection-map" markdown="1">
<div class="connection-hub" markdown="1">

**Operator computer**  
A ROS 2 environment matching the robot. The shared workstation's Ubuntu 24.04 installation does not by itself provide the legacy Foxy environment.

</div>
<div class="connection-branches" markdown="1">
<div class="connection-branch" markdown="1">

**Robot · network connection**

- Computer and Raspberry Pi join the same network.
- The Pi connects to the OpenCR board and LiDAR through the kit's data cables.
- The robot uses its matching battery and power wiring.

</div>
<div class="connection-branch" markdown="1">

**Optional · room tracking**

- OptiTrack cameras connect to the Motive system.
- Motive streams the tracked robot's position to the agreed receiving computer.
- The installed pose bridge makes that data available to ROS.

</div>
</div>
</div>

## 3. Assemble and connect

1. Follow the [Burger assembly manual](https://emanual.robotis.com/docs/en/platform/turtlebot3/hardware_setup/) for the delivered revision. Keep power off while checking internal connections.
2. Check that boards and the LiDAR are secure, wheels turn without catching cables, and no loose wire can touch the floor.
3. Have the installer inspect the battery and show the matching charging and shutdown procedures. Keep charging leads out of the driving area.
4. Join the robot and computer to the agreed network. Obtain credentials privately from the project owner.
5. Label each robot clearly. Keep its address, installed hardware revisions, and software versions in private setup notes.

**Next:** [Basic software](software.md).
