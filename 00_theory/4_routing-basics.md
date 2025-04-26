# 🚦 **Routing Basics: The Internet's Traffic Control System (And How Hackers Exploit It)**

Routing isn't just about connectivity - it's about **control**. Whoever controls the routes controls the traffic. Let's break down how it works and where the vulnerabilities lie.

---

## 📦 **Types of Routing: The Good, The Bad, and The Risky**

| Type       | Pros                  | Cons                  | Security Risk                  | Best For          |
|------------|-----------------------|-----------------------|--------------------------------|-------------------|
| **Static** | Simple, predictable   | Doesn't adapt         | 🚨 Manual errors = black holes | Small networks    |
| **Dynamic**| Self-healing          | Complex               | 🚨 Route poisoning attacks    | Enterprise nets   |
| **Default**| Catch-all safety net  | May create suboptimal paths | 🚨 Can leak internal traffic | Edge routers      |

💡 **Pro Tip**: In 2018, a **BGP hijack** by Russian ISP Rostelecom redirected traffic from AWS, Google, and others. Always verify routes!

---

## 🗺️ **Key Concepts Explained**

### **The Router: Internet's Traffic Cop**
- Connects different networks (like your office LAN to the internet)
- **Security Risk**: Compromised routers = complete network takeover
- **Defense**: Change default creds, disable telnet (use SSH)

### **Routing Table: The Router's Map**
```bash
# View routing table (Linux/Windows)
route print          # Windows
ip route show        # Linux
netstat -rn          # macOS