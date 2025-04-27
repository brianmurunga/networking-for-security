
---

### 📄 `packet-sniffing.md`

```markdown
# Packet Sniffing Basics

**Packet sniffing** is the process of intercepting and analyzing network traffic. Tools like Wireshark or tcpdump are commonly used.

---

## 🧩 Why Packet Sniff?

- Monitor real-time traffic for performance or security issues
- Understand how protocols operate at the packet level
- Investigate incidents like data leakage or malicious activity

---

## 🛠️ Tools for Sniffing

| Tool     | Description |
|----------|-------------|
| Wireshark | GUI-based, powerful packet analyzer |
| tcpdump   | CLI-based lightweight sniffer |
| TShark    | CLI version of Wireshark |

---

## 📡 Common Filters

- **Wireshark Display Filter:** `http.request`, `ip.addr == 192.168.1.1`
- **tcpdump Syntax:**  
  ```bash
  sudo tcpdump -i eth0 port 80
  sudo tcpdump -nn -X -s 0 -i eth0
