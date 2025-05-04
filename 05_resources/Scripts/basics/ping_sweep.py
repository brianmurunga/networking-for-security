import subprocess
import platform
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse

def ping_host(ip, count=1, timeout=1):
    """
    Ping a single IP address and return whether it is reachable.
    
    Args:
        ip (ipaddress.IPv4Address): IP to ping.
        count (int): Number of packets to send.
        timeout (int): Timeout in seconds for each packet.
        
    Returns:
        bool: True if the host is reachable, False otherwise.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, str(count), str(ip)]

    # Set timeout for ping command
    if platform.system().lower() == "windows":
        command += ["-w", str(timeout * 1000)]  # Windows uses milliseconds
    else:
        command += ["-W", str(timeout)]  # Unix-like uses seconds

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=count * timeout + 1  # Safety buffer
        )
        return result.returncode == 0
    except Exception:
        return False

def sweep_network(network, count=1, timeout=1, threads=100):
    """
    Ping all usable hosts in the given network concurrently.
    
    Args:
        network (ipaddress.IPv4Network): The network to scan.
        count (int): Number of packets to send per host.
        timeout (int): Timeout in seconds for each ping.
        threads (int): Number of concurrent threads to use.
        
    Returns:
        list: List of reachable IP addresses.
    """
    live_hosts = []
    print(f"Pinging all hosts in {network}...\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(ping_host, ip, count, timeout): ip for ip in network.hosts()}

        for future in as_completed(futures):
            ip = futures[future]
            try:
                if future.result():
                    print(f"[+] Host {ip} is UP")
                    live_hosts.append(str(ip))
                else:
                    print(f"[-] Host {ip} is DOWN")
            except Exception as e:
                print(f"[!] Error pinging {ip}: {e}")

    return live_hosts

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ping a network range to find live hosts.")
    parser.add_argument("network", help="Network in CIDR notation (e.g., 192.168.1.0/24)")
    parser.add_argument("--count", type=int, default=1, help="Number of packets to send per host")
    parser.add_argument("--timeout", type=int, default=1, help="Timeout in seconds for each ping")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads to use")

    args = parser.parse_args()

    try:
        network = ipaddress.IPv4Network(args.network)
        live_hosts = sweep_network(network, args.count, args.timeout, args.threads)

        print("\n=== Scan Complete ===")
        print(f"Total hosts scanned: {network.num_addresses - 2}")
        print(f"Live hosts detected: {len(live_hosts)}")
        print("Live hosts:")
        for host in live_hosts:
            print(f" - {host}")

    except ValueError as e:
        print(f"[!] Invalid network: {e}")