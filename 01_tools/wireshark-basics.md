# Wireshark Basics

**Wireshark** is a powerful packet analyzer used for network troubleshooting, analysis, and cybersecurity tasks.

---

## 🧩 What is Wireshark?

- Open-source network protocol analyzer
- Captures packets in real-time and displays them in a readable format
- Useful for learning and debugging network behavior

---

## 🖥️ Installing Wireshark

- [Download](https://www.wireshark.org/download.html) for Windows, macOS, Linux
- Run with administrator/root privileges to capture packets

---

## 📡 Capturing Packets

1. Open Wireshark
2. Select a network interface (e.g., `eth0`, `wlan0`)
3. Click "Start Capturing"
4. Use filters (e.g., `http`, `ip.addr == 192.168.1.1`) to focus data

---

## 🔍 Key Features

- **Display Filters:** Focus on specific traffic (e.g., `tcp.port == 80`)
- **Follow Streams:** Reconstruct conversations (TCP streams)
- **Color Coding:** Highlights protocol-specific traffic
- **Expert Info:** Warnings for malformed or suspicious packets

---

## 🔐 Common Use Cases

- Identify slow network behavior
- Analyze HTTP, DNS, DHCP, etc.
- Investigate security issues or attacks

---

## 📌 Summary
- Wireshark is essential for analyzing real-time packet flows
- Great for understanding how protocols behave under the hood
- Display filters make analysis efficient
