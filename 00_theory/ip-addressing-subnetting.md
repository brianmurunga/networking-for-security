# IP Addressing & Subnetting
# 1
IP addresses are unique identifiers for devices on a network. Subnetting allows you to divide networks for better organization and security.

---

## 📌 IP Address Structure

An IPv4 address is a 32-bit number, written as four decimal octets:  
`192.168.1.15`

Each IP address has:
- **Network portion** – identifies the network
- **Host portion** – identifies the device on that network
- Example IP Address: 192.168.1.1 (with subnet mask 255.255.255.0)
- Network portion = 192.168.1 (all devices in this network share this part).
- Host portion = .15 (uniquely identifies a specific device, like a computer or phone).
- This means:
- Any device with an IP starting with 192.168.1 (e.g., 192.168.1.1, 192.168.1.15) is on the same network.

---

## 🎯 Classes of IP Addresses

| Class | Range           | Default Subnet Mask | Usage         |
|-------|------------------|----------------------|---------------|
| A     | 1.0.0.0 – 126.0.0.0 | 255.0.0.0        | Large networks |
| B     | 128.0.0.0 – 191.255.0.0 | 255.255.0.0 | Medium networks |
| C     | 192.0.0.0 – 223.255.255.0 | 255.255.255.0 | Small networks |

---

## 🔐 Private IP Ranges
- Private IP addresses are like "internal phone numbers" used inside your home or office network, they cannot be used on the public Internet.

- Class A: 10.0.0.0 – 10.255.255.255  
- Class B: 172.16.0.0 – 172.31.255.255  
- Class C: 192.168.0.0 – 192.168.255.255  

# Why These Ranges?
1. Private & Reusable: Unlike public IPs, these can be used by anyone inside their own network.
2. NAT Helps: Your router uses Network Address Translation (NAT) to share one public IP for all private devices.
- No Internet Direct Access: If you try to ping 192.168.1.1 from outside, it won’t work—it’s only for local networks.
---

## 📐 Subnetting

**Subnetting** divides a large network into smaller sub-networks (subnets).


-Original: 192.168.1.0/24 (256 IPs, 254 usable)
**Subnetted:**
## Original Network: `192.168.1.0/24`

- The `/24` notation indicates that the first 24 bits are used for the network portion, leaving 8 bits for host addresses.
- Total IPs = $ 2^8 = 256 $
- Usable IPs = $ 256 - 2 = 254 $ (subtracting the network address and broadcast address).

### Address Range:
- **Network Address**: `192.168.1.0`
- **Broadcast Address**: `192.168.1.255`
- **Usable IPs**: `192.168.1.1` to `192.168.1.254`

---

## Subnetting into `/25`

When you subnet the original `/24` network into two `/25` subnets:
- The `/25` notation means the first 25 bits are used for the network portion, leaving 7 bits for host addresses.
- Total IPs per subnet = $ 2^7 = 128 $
- Usable IPs per subnet = $ 128 - 2 = 126 $

### First Subnet: `192.168.1.0/25`
- **Network Address**: `192.168.1.0`
- **Broadcast Address**: `192.168.1.127`
- **Usable IPs**: `192.168.1.1` to `192.168.1.126`

### Second Subnet: `192.168.1.128/25`
- **Network Address**: `192.168.1.128`
- **Broadcast Address**: `192.168.1.255`
- **Usable IPs**: `192.168.1.129` to `192.168.1.254`

---

## Verification
The original `/24` network has been successfully divided into two `/25` subnets:
1. Each subnet has exactly half the number of IPs as the original network (128 IPs per subnet).
2. The two subnets do not overlap and fully utilize the original IP range (`192.168.1.0` to `192.168.1.255`).

---
### 2. CIDR Notation (`/24`, `/16`, etc.)
- Indicates **fixed network bits**:
  - `/24` = `255.255.255.0` (Class C)
  - `/16` = `255.255.0.0` (Class B)
  - `/8` = `255.0.0.0` (Class A)


### 3. Why Subnet?
| Benefit          | Explanation                          | Analogy                     |
|------------------|--------------------------------------|-----------------------------|
| **Traffic Control** | Reduces congestion by isolating traffic | Separate lanes on a highway |
| **Security**     | Isolates breaches (e.g., HR vs. Guest) | Locked office departments   |
| **Efficient IPs** | Prevents IP wastage                   | Assigning only needed seats |

---

## 🔧 Tools

### **Subnet Calculators**
- [ipcalc (Online)](https://jodies.de/ipcalc) - Visual subnet range calculator
- [CIDR.xyz (Interactive)](https://cidr.xyz/) - Play with CIDR blocks in real-time
- [SolarWinds Subnet Calculator (Download)](https://www.solarwinds.com/free-tools/subnet-calculator) - Advanced subnetting tool
- **Command-Line Tools**:
  ```bash
  # Linux (ipcalc)
  sudo apt install ipcalc
  ipcalc 192.168.1.0/24

  # Windows (built-in)
  netsh interface ip show config

---

## 📌 Summary
- Subnetting is essential for efficient and secure network design
