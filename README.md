# Net_Scan

A simple Python CLI tool for scanning and listing devices connected to a network.

## Features

- Scans a given IP range to find connected devices
- Displays IP and MAC addresses of connected devices
- Verbose mode for detailed output

## Requirements

- Python 3.6+
- Scapy library
- [Npcap](https://nmap.org/npcap/) (Windows users)

## Installation

### Step 1: Install Npcap (Windows Users)

If you're using Windows, you need to install Npcap, which is required for packet capturing. Follow these steps:

1. **Download and Install Npcap**:
   - Go to the [Npcap website](https://nmap.org/npcap/) and download the latest installer.
   - Run the installer and follow the prompts. Make sure to check the box for "Install Npcap in WinPcap API-compatible mode" during installation.

### Step 2: Clone the Repository

```sh
git clone https://github.com/yourusername/network-scanner.git
cd network-scanner
