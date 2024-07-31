import scapy.all as scapy
import argparse
import ctypes
import os
import sys

def get_arguments():
    parser = argparse.ArgumentParser(description="Network Scanner Tool")
    parser.add_argument("-t", "--target", dest="target", required=True, help="Target IP range (e.g., 192.168.1.1/24)")
    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    return args

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def scan(ip, verbose=False):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=verbose)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP Address\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")

if __name__ == "__main__":
    if is_admin():
        arguments = get_arguments()
        if arguments.verbose:
            print(f"Scanning network: {arguments.target}")
        scan_result = scan(arguments.target, arguments.verbose)
        print_result(scan_result)
    else:
        print("This script requires administrative privileges to run.")
        if sys.version_info[0] == 3:
            # Prompt to rerun with admin privileges
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
