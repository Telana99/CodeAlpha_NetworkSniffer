from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        # Identify protocol name
        if TCP in packet:
            proto_name = "TCP"
            payload = bytes(packet[TCP].payload)
        elif UDP in packet:
            proto_name = "UDP"
            payload = bytes(packet[UDP].payload)
        elif ICMP in packet:
            proto_name = "ICMP"
            payload = bytes(packet[ICMP].payload)
        else:
            proto_name = str(protocol)
            payload = b""

        print(f"[{proto_name}] {src_ip} --> {dst_ip} | Payload size: {len(payload)} bytes")
        if payload:
            print(f"       Payload (first 50 bytes): {payload[:50]}")
        print("-" * 60)

print("🔍 Starting Network Sniffer... Press CTRL+C to stop\n")
sniff(filter="ip", prn=packet_handler, store=0)