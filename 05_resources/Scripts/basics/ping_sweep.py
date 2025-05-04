# A simple tool to ping a range of IP addresses to find live hosts.

import subprocess
import platform
import ipaddress

def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip)]
    result = subprocess.run(command, stdout=subprocess.DEVNULL)
    return result.returncode == 0

def sweep_network(network):
    print(f"Pinging all hosts in {network}...\n")
    live_hosts = []
    for ip in ipaddress.IPv4Network(network):
        if ip.exploded.endswith(".0") or ip.exploded.endswith(".255"):
            continue
        if ping_host(ip):
            print(f"[+] Host {ip} is UP")
            live_hosts.append(str(ip))
        else:
            print(f"[-] Host {ip} is DOWN")
    return live_hosts

if __name__ == "__main__":
    net = input("Enter network (e.g., 192.168.1.0/24): ")
    sweep_network(net)
