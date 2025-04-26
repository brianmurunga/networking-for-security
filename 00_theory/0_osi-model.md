# OSI Model (Open Systems Interconnection)

The **OSI Model** is a conceptual framework used to understand how data moves through a network. It divides networking into **7 layers**, each with specific functions.

---

## The 7 Layers of the OSI Model

| Layer | Name             | Description |
|-------|------------------|---------------------------------------------------|
| 7     | Application      | Interface for user applications (e.g., HTTP, FTP) |
| 6     | Presentation     | Data formatting, encryption, compression          |
| 5     | Session          | Manages sessions and controls dialogues           |
| 4     | Transport        | Reliable data transfer (TCP/UDP)                  |
| 3     | Network          | Routing and addressing (IP)                       |
| 2     | Data Link        | MAC addressing, frame delivery (Ethernet)         |
| 1     | Physical         | Actual hardware transmission (cables, bits)       |

---

## Mnemonic (Top to Bottom)
**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing
my favourite one at school was as below in _ascending order_
**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

---

## OSI Model & Security
- Firewalls operate at Layers 3-4
- Packet filtering uses Layer 3 (IP) and Layer 4 (TCP/UDP)
- Deep packet inspection can reach up to Layer 7

---

## Summary
- OSI is theoretical, but important for understanding protocols
- Real-world networking often uses TCP/IP model
