# 🔍 Basic Network Sniffer

A Python-based network packet sniffer built using **Scapy** that captures and analyzes live network traffic in real time.

---

## 📌 Project Overview

This project was developed as part of the **CodeAlpha Cybersecurity Internship – Task 1**.

The sniffer captures network packets flowing through your system and displays useful information including:
- Source and Destination IP addresses
- Protocol type (TCP, UDP, ICMP)
- Payload size and content preview

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Scapy** – Packet capture and analysis library
- **Npcap** – Windows packet capture driver

---

## 📋 Requirements

- Python 3.7 or higher
- Scapy 2.x
- Npcap (Windows only) – [Download here](https://npcap.com/#download)

### Install dependencies:
```bash
pip install scapy
pip install pywin32   # Windows only
```

---

## 🚀 How to Run

> ⚠️ **Must be run as Administrator** (required for packet sniffing)

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_NetworkSniffer
cd CodeAlpha_NetworkSniffer
```

2. Run the sniffer:
```bash
python sniffer.py
```

3. Open your browser or any app to generate traffic — packets will appear in the terminal.

4. Press **CTRL + C** to stop.

---

## 📊 Sample Output

```
🔍 Starting Network Sniffer... Press CTRL+C to stop

[TCP] 192.168.1.16 --> 142.250.180.46 | Payload size: 120 bytes
       Payload (first 50 bytes): b'\x17\x03\x03\x00i\x10...'
------------------------------------------------------------
[UDP] 8.8.8.8 --> 192.168.1.16 | Payload size: 77 bytes
       Payload (first 50 bytes): b'd2:ip6:p\x86\xb5W...'
------------------------------------------------------------
```

---

## 🔎 Understanding the Output

| Field | Description |
|---|---|
| `[TCP]` / `[UDP]` / `[ICMP]` | Network protocol used |
| Source IP | Where the packet came from |
| Destination IP | Where the packet is going |
| Payload size | Amount of data in bytes |
| Payload preview | First 50 bytes of raw data |

---

## 📁 Project Structure

```
CodeAlpha_NetworkSniffer/
│
├── sniffer.py       # Main network sniffer script
└── README.md        # Project documentation
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**. Only use it on networks you own or have explicit permission to monitor. Unauthorized packet sniffing is illegal.

---

## 👤 Author

- **Internship:** CodeAlpha Cybersecurity Internship
- **Task:** Task 1 – Basic Network Sniffer
