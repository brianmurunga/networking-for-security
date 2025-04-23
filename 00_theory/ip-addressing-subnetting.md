# IP Addressing & Subnetting

IP addresses are unique identifiers for devices on a network. Subnetting allows you to divide networks for better organization and security.

---

## 📌 IP Address Structure

An IPv4 address is a 32-bit number, written as four decimal octets:  
`192.168.1.1`

Each IP address has:
- **Network portion** – identifies the network
- **Host portion** – identifies the device on that network

---

## 🎯 Classes of IP Addresses

| Class | Range           | Default Subnet Mask | Usage         |
|-------|------------------|----------------------|---------------|
| A     | 1.0.0.0 – 126.0.0.0 | 255.0.0.0        | Large networks |
| B     | 128.0.0.0 – 191.255.0.0 | 255.255.0.0 | Medium networks |
| C     | 192.0.0.0 – 223.255.255.0 | 255.255.255.0 | Small networks |

---

## 🔐 Private IP Ranges

- Class A: 10.0.0.0 – 10.255.255.255  
- Class B: 172.16.0.0 – 172.31.255.255  
- Class C: 192.168.0.0 – 192.168.255.255  

---

## 📐 Subnetting

**Subnetting** divides a large network into smaller sub-networks (subnets).

- Example: `192.168.1.0/24` = 256 IPs (254 usable)
- CIDR notation (`/24`, `/16`, etc.) shows how many bits are fixed

Subnetting helps with:
- Traffic management
- Isolation for security
- Efficient IP usage

---

## 🔧 Tools
- Subnet calculators (online or command-line)
- Binary conversion practice

---

## 📌 Summary
- Understand classes, private vs public IPs
- Learn CIDR, subnet masks, usable IPs
- Subnetting is essential for efficient and secure network design
