#!/usr/bin/env python3
"""
Get My IP - Display both public and private IP addresses
"""

import socket
import requests
import argparse
from requests.exceptions import RequestException

def get_private_ip():
    """Get the machine's private IP address"""
    try:
        # Create a socket connection to get the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google DNS
        private_ip = s.getsockname()[0]
        s.close()
        return private_ip
    except Exception as e:
        return f"Error getting private IP: {str(e)}"

def get_public_ip():
    """Get the machine's public IP address using external services"""
    services = [
        'https://api.ipify.org',
        'https://ident.me',
        'https://ifconfig.me/ip',
        'https://ipinfo.io/ip'
    ]
    
    for service in services:
        try:
            response = requests.get(service, timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except RequestException:
            continue
    
    return "Unable to determine public IP (no internet connection or all services failed)"

def display_ip_info(show_private=True, show_public=True):
    """Display IP information based on user preferences"""
    if show_private:
        private_ip = get_private_ip()
        print(f"Private IP Address: {private_ip}")
    
    if show_public:
        public_ip = get_public_ip()
        print(f"Public IP Address:  {public_ip}")

def main():
    """Parse arguments and display IP information"""
    parser = argparse.ArgumentParser(description="Display your public and private IP addresses")
    parser.add_argument("--private-only", action="store_true", 
                       help="Show only private IP address")
    parser.add_argument("--public-only", action="store_true", 
                       help="Show only public IP address")
    
    args = parser.parse_args()
    
    show_private = not args.public_only
    show_public = not args.private_only
    
    if args.private_only and args.public_only:
        print("Cannot specify both --private-only and --public-only")
        return
    
    display_ip_info(show_private, show_public)

if __name__ == "__main__":
    main()