# 🔒 **VLANs & Trunking: Network Segmentation for Security and Performance**

VLANs are like **building separate virtual highways** on the same physical network - keeping traffic isolated and secure. But misconfigured VLANs can become a hacker's playground.

---

## 🧩 **VLANs Explained: More Than Just Segmentation**

### **Why VLANs Matter**
- **Security**: Isolate sensitive departments (HR, Finance)
- **Performance**: Reduce unnecessary broadcast traffic
- **Flexibility**: Group devices by function, not location

### **Common VLAN Types**
| VLAN Type       | Purpose                          | Security Consideration         |
|-----------------|----------------------------------|--------------------------------|
| **Data VLAN**   | Regular user traffic             | 🚨 Default VLAN 1 is vulnerable |
| **Voice VLAN**  | VoIP phone traffic               | 🚨 QoS bypass attacks possible |
| **Native VLAN** | Untagged trunk traffic           | 🚨 #1 target for VLAN hopping  |
| **Management VLAN** | Switch administration       | 🚨 Should NEVER be VLAN 1      |

💡 **Pro Tip**: Always change the native VLAN from default (VLAN 1) to an unused VLAN number.

---

## 🏗️ **VLAN Configuration: Cisco/Nexus Examples**

### **Basic VLAN Setup**
```cisco
! Create VLANs
vlan 10
  name HR
vlan 20
  name Finance

! Assign access ports
interface Gig1/0/1
  switchport mode access
  switchport access vlan 10
  switchport nonegotiate  # Disable DTP