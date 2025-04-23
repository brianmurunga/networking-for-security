
---

#### 📄 `nat-pat.md`

```markdown
# NAT & PAT

**NAT (Network Address Translation)** allows private IPs to access public networks.  
**PAT (Port Address Translation)** allows multiple devices to share a single public IP.

---

## 🌍 Why NAT?

- Conserves public IP addresses
- Hides internal IP structure
- Enhances security through IP masking

---

## 🧩 Types of NAT

| Type         | Description                           |
|--------------|----------------------------------------|
| Static NAT   | One-to-one mapping (inside ↔ public IP) |
| Dynamic NAT  | Pool of public IPs for internal devices |
| PAT (NAT Overload) | Many-to-one mapping using ports |

---

## 🔧 PAT Example (Cisco)

```bash
ip nat inside source list 1 interface fa0/1 overload
access-list 1 permit 192.168.1.0 0.0.0.255
interface fa0/0
ip nat inside
interface fa0/1
ip nat outside
