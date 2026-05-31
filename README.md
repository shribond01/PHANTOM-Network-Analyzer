# PHANTOM Network Analyzer

## 1. Introduction

PHANTOM Network Analyzer is a Python-based network packet sniffer developed using Scapy on Kali Linux. The project captures and analyzes network traffic in real time, allowing users to observe communication between devices on a network.

---

## 2. Objective

The objective of this project is to understand network communication by capturing packets and identifying protocols such as TCP, UDP, and ICMP. The project also aims to provide basic packet statistics and logging functionality.

---

## 3. Technologies Used

* Python
* Scapy
* Kali Linux
* GitHub

---

## 4. Features

* Real-time packet capture
* TCP packet detection
* UDP packet detection
* ICMP packet detection
* Source and destination IP analysis
* Packet statistics generation
* Log file creation

---

## 5. Methodology

1. Capture packets using Scapy's sniff() function.
2. Analyze packet contents.
3. Identify the protocol type.
4. Display packet information.
5. Store packet details in a log file.
6. Generate statistics after packet capture is completed.

---

## 6. Results

The application successfully captured network packets and classified them based on protocol type. Statistics were generated showing the total number of packets captured and protocol distribution.

Example Output:

* Total Packets: 200
* UDP Packets: 5
* ICMP Packets: 1
* Other Packets: 194

---

## 7. Learning Outcomes

Through this project, I gained practical experience in:

* Packet sniffing
* Network traffic analysis
* TCP, UDP, and ICMP protocols
* Python networking libraries
* Cybersecurity monitoring concepts

---

## 8. Future Enhancements

* ARP packet detection
* DNS traffic analysis
* Threat detection features
* CSV report export
* Real-time dashboard

---

## 9. Conclusion

PHANTOM Network Analyzer successfully demonstrates the fundamentals of packet capture and network analysis. The project provided hands-on experience with networking concepts and cybersecurity monitoring using Python and Scapy.
