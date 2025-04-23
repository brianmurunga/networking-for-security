# VLANs & Trunking

**VLANs (Virtual Local Area Networks)** allow logical segmentation of networks at Layer 2, improving organization and security.

---

## 🧩 What is a VLAN?

- A **VLAN** groups devices logically, not physically
- Devices in the same VLAN can communicate as if they're on the same switch
- VLANs reduce broadcast domains

Example:
- VLAN 10 = HR
- VLAN 20 = Finance

---

## 🏗️ VLAN Configuration (Cisco Syntax)

```bash
Switch(config)# vlan 10
Switch(config-vlan)# name HR
Switch(config)# interface fa0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
