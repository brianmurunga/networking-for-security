import ipaddress
import unittest

__author__ = "brian murunga | c0mmand3r"
__version__ = "1.1"  # Update version in case of major changes

def calculate_network_details(network_str):
    """
    Calculate and display details of a given IP network.

    Args:
        network_str (str): The IP network in CIDR notation (e.g., '192.168.1.0/24').

    Returns:
        dict: A dictionary containing the network details, or None if invalid.
    """
    if not network_str:
        print("Error: Network input cannot be empty.")
        return None
    try:
        net = ipaddress.ip_network(network_str, strict=False)
        num_addresses = net.num_addresses
        usable_ips = num_addresses - 2 if num_addresses > 2 else 0
        ip_range = f"{net[0] + 1} - {net[-2]}" if num_addresses > 2 else "N/A" if num_addresses > 0 else "N/A"

        network_details = {
            "Network Address": str(net.network_address),
            "Broadcast Address": str(net.broadcast_address),
            "Total IPs": num_addresses,
            "Usable IPs": usable_ips,
            "IP Range": ip_range,
            "Subnet Mask": str(net.netmask),
        }
        return network_details
    except ipaddress.AddressValueError:
        print(f"Error: Invalid IP address format: '{network_str}'.")
        return None
    except ipaddress.NetmaskValueError:
        print(f"Error: Invalid CIDR prefix in '{network_str}'.")
        return None
    except ValueError as e:
        print(f"An unexpected error occurred: {e}") # Catch other ValueErrors
        return None

def main():
    """
    Main function to interact with the user and display network details.
    """
    print(f"=== IP Network Calculator v{__version__} ===")
    print(f"Developed by: {__author__}\n")
    while True:
        network_input = input("Enter the network in CIDR notation (e.g., 192.168.1.0/24) or type 'exit': ").strip()
        if network_input.lower() == 'exit':
            break

        details = calculate_network_details(network_input)

        if details:
            print("\nNetwork Details:")
            for key, value in details.items():
                print(f"  {key}: {value}")
        print("-" * 20)

class TestNetworkDetails(unittest.TestCase):

    def test_valid_network(self):
        details = calculate_network_details("192.168.1.0/24")
        self.assertEqual(details["Network Address"], "192.168.1.0")
        self.assertEqual(details["Broadcast Address"], "192.168.1.255")
        self.assertEqual(details["Total IPs"], 256)
        self.assertEqual(details["Usable IPs"], 254)
        self.assertEqual(details["IP Range"], "192.168.1.1 - 192.168.1.254")
        self.assertEqual(details["Subnet Mask"], "255.255.255.0")

    def test_single_host_network(self):
        details = calculate_network_details("10.0.0.1/32")
        self.assertEqual(details["Total IPs"], 1)
        self.assertEqual(details["Usable IPs"], 0)
        self.assertEqual(details["IP Range"], "N/A")

    def test_point_to_point_network(self):
        details = calculate_network_details("172.16.0.0/31")
        self.assertEqual(details["Total IPs"], 2)
        self.assertEqual(details["Usable IPs"], 0)
        self.assertEqual(details["IP Range"], "N/A")

    def test_invalid_network_format(self):
        details = calculate_network_details("192.168.1.0")
        self.assertIsNone(details)

    def test_invalid_cidr(self):
        details = calculate_network_details("192.168.1.0/33")
        self.assertIsNone(details)

    def test_empty_input(self):
        details = calculate_network_details("")
        self.assertIsNone(details)

if __name__ == "__main__":
    # Run the main function if the script is executed directly
    if __name__ == "__main__":
        main()

    # Run the unit tests if the script is executed with the 'unittest' module
    if __name__ == "__main__":
        unittest.main(argv=['first-arg-is-ignored'], exit=False)