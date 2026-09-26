# Prepare the workstation

**Goal:** prepare one shared desktop for VLA Pipeline, Self Improvement Learning, and ABC Box.

## 1. Check the delivered computer

Use the [workstation specification](hardware.md#workstation-specification-for-vla-pipeline-and-self-improvement-learning). Confirm the **RTX PRO 6000 Blackwell Workstation Edition, 96 GB**, plus the agreed CPU, system memory, storage, and network/USB connections.

Have the supplier confirm that the case, motherboard, power supply, and cooling support the selected card. The reference inventory is not a complete list of compatible parts for a new computer.

## 2. Position and connect it

1. Place the computer where its air vents remain clear and robot movement cannot reach it.
2. Connect the monitor, keyboard, mouse, and the approved mains lead.
3. Connect the workstation to the lab network switch/router with Ethernet.
4. Label the workstation, its network cable, and the ports used by each platform.
5. Arrange a backup destination and enough free storage for the expected recordings.

Keep power strips, connectors, and loose cable loops away from the robots and walking area. Follow the supplier's electrical and ventilation requirements.

## 3. Plan the device connections

| Device group | Connection to prepare |
|---|---|
| Two xArm control boxes | One Ethernet connection per controller to the shared network |
| Five xArm cameras | USB data connections with enough bandwidth for the intended simultaneous views |
| Quest headsets | One data-capable USB connection per headset used |
| Three ABC Box cameras | USB data connections for two wrist views and one overhead view |
| ABC Box followers and leaders | Supplier-approved control interfaces connected to the shared workstation |
| Go2 onboard computer | The lab's approved Ethernet or wireless connection |
| Monitor and input devices | Suitable display and USB connections |

More USB sockets do not necessarily mean more bandwidth: several sockets can share one internal connection. Have the installer check all intended camera views for the active platform together, and use an approved powered hub only when the layout calls for one. The dog's D435i connects to the onboard computer, not to the desk workstation.

## 4. Check the workstation before handover

- [ ] Selected GPU and agreed CPU, memory, and storage are recorded.
- [ ] Power, cooling, monitor, keyboard, and mouse work.
- [ ] Network connections reach the intended equipment.
- [ ] Cameras and headsets have labeled data-capable cables.
- [ ] All required camera views can be checked together by the installer.
- [ ] Storage, backup, and use of the shared computer are arranged.

**Next:** check the connections for [VLA Pipeline](../vla-pipeline/hardware/index.md), [Self Improvement Learning](../unidog-nav/hardware.md), or [ABC Box](../abc-box/hardware.md).
