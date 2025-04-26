
---

#### 📄 `acls.md`

```markdown
# Access Control Lists (ACLs)

**ACLs** are filters used to control traffic based on rules. Commonly applied on routers and firewalls.

---

## 🛡️ What ACLs Can Do

- Permit or deny specific IPs or subnets
- Block or allow specific ports/protocols
- Apply security policies per interface

---

## 🔢 Types of ACLs

| Type      | Description                    |
|-----------|--------------------------------|
| Standard  | Filters by source IP only      |
| Extended  | Filters by source, destination, port, protocol |

---

## 🔧 Standard ACL Example (Cisco)

```bash
access-list 10 permit 192.168.1.0 0.0.0.255
interface fa0/0
ip access-group 10 in
