# Nmap Introduction

**Nmap (Network Mapper)** is a free and open-source tool for network discovery and security auditing.

---

## 🔎 What Can Nmap Do?

- Scan IP addresses, ports, and services
- Identify devices on a network
- Detect operating systems and versions
- Perform security audits

---


## 🛠️ Installation

```bash
sudo apt install nmap         # Debian/Ubuntu
brew install nmap             # macOS (Homebrew)
choco install nmap            # Windows (Chocolatey)

---
Command | Purpose
- nmap <IP> | Basic scan
- nmap -sS <IP> | Stealth SYN scan
- nmap -sV <IP> | Detect services/versions
- nmap -O <IP> | OS detection
- nmap -p 1-1000 <IP> | Scan specific port range
- nmap -s -A <IP> | Aggressive scan on all ports, not recommended for unauthorized networks