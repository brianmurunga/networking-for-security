#!/usr/bin/env python3
"""
Packet Sniffer with filtering and better output formatting
"""

from scapy.all import sniff, Ether, IP, TCP, UDP, ARP, ICMP
import argparse
import signal
import sys
from datetime import datetime

def signal_handler(sig, frame):
    """Handle CTRL+C gracefully"""
    print("\nSniffing stopped by user.")
    sys.exit(0)

def packet_callback(packet, verbose=False):
    """Enhanced packet processing with better formatting"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
    if packet.haslayer(Ether):
        eth_src = packet[Ether].src
        eth_dst = packet[Ether].dst
        eth_type = packet[Ether].type
        base_info = f"[{timestamp}] ETH {eth_src} -> {eth_dst} (Type: 0x{eth_type:04x})"
    else:
        base_info = f"[{timestamp}] RAW Packet"
    
    # Process different protocol layers
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        base_info += f" | IP {ip_layer.src} -> {ip_layer.dst} Proto: {ip_layer.proto}"
        
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            base_info += f" | TCP {tcp_layer.sport} -> {tcp_layer.dport} Flags: {tcp_layer.flags}"
            if verbose and tcp_layer.payload:
                base_info += f"\n    Payload: {bytes(tcp_layer.payload)[:100]}"
                
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            base_info += f" | UDP {udp_layer.sport} -> {udp_layer.dport}"
            if verbose and udp_layer.payload:
                base_info += f"\n    Payload: {bytes(udp_layer.payload)[:100]}"
                
    elif packet.haslayer(ARP):
        arp_layer = packet[ARP]
        base_info += f" | ARP {arp_layer.psrc} -> {arp_layer.pdst} ({'request' if arp_layer.op == 1 else 'reply'})"
        
    elif packet.haslayer(ICMP):
        icmp_layer = packet[ICMP]
        base_info += f" | ICMP Type: {icmp_layer.type} Code: {icmp_layer.code}"
    
    print(base_info)

def start_sniffing(interface=None, filter_expr=None, count=0, verbose=False):
    """Start packet sniffing with configurable options"""
    print(f"\nStarting packet sniffing on {interface or 'default interface'}...")
    if filter_expr:
        print(f"Filter: {filter_expr}")
    print("Press CTRL+C to stop\n")
    
    try:
        sniff(
            iface=interface,
            prn=lambda pkt: packet_callback(pkt, verbose),
            filter=filter_expr,
            count=count,
            store=False
        )
    except PermissionError:
        print("Error: Requires root privileges to sniff packets")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """Parse arguments and start sniffing"""
    parser = argparse.ArgumentParser(description="Advanced Packet Sniffer")
    parser.add_argument("-i", "--interface", help="Network interface to sniff on")
    parser.add_argument("-f", "--filter", help="BPF filter expression (e.g., 'tcp port 80')")
    parser.add_argument("-c", "--count", type=int, default=0, 
                       help="Number of packets to capture (0 for unlimited)")
    parser.add_argument("-v", "--verbose", action="store_true", 
                       help="Show more detailed packet information")
    
    args = parser.parse_args()
    
    # Register CTRL+C handler
    signal.signal(signal.SIGINT, signal_handler)
    
    start_sniffing(
        interface=args.interface,
        filter_expr=args.filter,
        count=args.count,
        verbose=args.verbose
    )

if __name__ == "__main__":
    main()