from scapy.all import sniff, IP, TCP, UDP, ICMP, conf

# Function to process each captured packet
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if TCP in packet:
            protocol = "TCP"
            payload = packet[TCP].payload
        elif UDP in packet:
            protocol = "UDP"
            payload = packet[UDP].payload
        elif ICMP in packet:
            protocol = "ICMP"
            payload = packet[ICMP].payload
        else:
            payload = packet[IP].payload

        print(f"Source: {ip_src} -> Destination: {ip_dst} | Protocol: {protocol} | Payload: {payload}")

# Function to start packet sniffing
def start_sniffing(interface=None):
    conf.L3socket = conf.L3socket  # Set the default L3 socket
    if interface:
        sniff(prn=packet_callback, iface=interface, store=0)
    else:
        sniff(prn=packet_callback, store=0)

# Ensure to run this script with root privileges
if __name__ == "__main__":
    interface = input("Enter the network interface to sniff on (or press Enter to sniff on all interfaces): ")
    start_sniffing(interface)

