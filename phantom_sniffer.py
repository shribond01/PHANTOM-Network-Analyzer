from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

# ==========================================
# PHANTOM NETWORK ANALYZER v2.0
# ==========================================

total_packets = 0
tcp_packets = 0
udp_packets = 0
icmp_packets = 0
other_packets = 0

log_file = open("phantom_log.txt", "a")


def process_packet(packet):

    global total_packets
    global tcp_packets
    global udp_packets
    global icmp_packets
    global other_packets

    total_packets += 1

    timestamp = datetime.now().strftime("%H:%M:%S")

    if IP in packet:

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
            tcp_packets += 1

        elif UDP in packet:
            protocol = "UDP"
            udp_packets += 1

        elif ICMP in packet:
            protocol = "ICMP"
            icmp_packets += 1

        else:
            other_packets += 1

        print("\n" + "=" * 60)
        print(f"Packet #{total_packets}")
        print(f"Time: {timestamp}")
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")
        print(f"Protocol       : {protocol}")
        print("=" * 60)

        log_file.write(
            f"[{timestamp}] "
            f"{src_ip} -> {dst_ip} "
            f"{protocol}\n"
        )

    else:
        other_packets += 1


print("=" * 60)
print("PHANTOM NETWORK ANALYZER v2.0")
print("Capturing 200 Packets...")
print("=" * 60)

sniff(
    prn=process_packet,
    store=False,
    count=200
)

print("\n")
print("=" * 60)
print("PHANTOM NETWORK ANALYZER REPORT")
print("=" * 60)

print(f"Total Packets : {total_packets}")
print(f"TCP Packets   : {tcp_packets}")
print(f"UDP Packets   : {udp_packets}")
print(f"ICMP Packets  : {icmp_packets}")
print(f"Other Packets : {other_packets}")

print("=" * 60)

log_file.close()
