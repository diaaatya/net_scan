
# Net Scan User Guide

This user guide provides detailed instructions on how to install, configure, and use the Net Scan CLI tool.

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
   - [Step 1: Install Npcap (Windows Users)](#step-1-install-npcap-windows-users)
   - [Step 2: Clone the Repository](#step-2-clone-the-repository)
   - [Step 3: Install the Required Libraries](#step-3-install-the-required-libraries)
4. [Usage](#usage)
   - [Basic Usage](#basic-usage)
   - [Verbose Mode](#verbose-mode)
   - [Arguments](#arguments)
5. [Examples](#examples)
6. [Troubleshooting](#troubleshooting)
7. [License](#license)
8. [Contributing](#contributing)
9. [Issues](#issues)

## Introduction

The Network Scanner is a simple Python CLI tool designed to scan and list devices connected to a network. It displays the IP and MAC addresses of connected devices and provides a verbose mode for detailed output.

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

1. **Clone the repository**:

   ```sh
   git clone https://github.com/diaaatya/net_scan.git
   cd network-scanner
   ```

### Step 3: Install the Required Libraries

1. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

   This command installs the necessary dependencies listed in `requirements.txt`.

## Usage

### Basic Usage

To scan a specific IP range and list the connected devices, run the script with the `-t` or `--target` argument followed by the target IP range.

```sh
python net_scan.py -t 192.168.1.1/24
```

### Verbose Mode

For more detailed output during the scanning process, use the `-v` or `--verbose` flag.

```sh
python net_scan.py -t 192.168.1.1/24 -v
```

### Arguments

- `-t`, `--target`: **Required.** Specifies the target IP range to scan (e.g., `192.168.1.1/24`).
- `-v`, `--verbose`: Optional. Enables verbose output for more detailed information.

## Examples

### Basic Scan

To perform a basic scan of the network in the IP range `192.168.1.1/24`:

```sh
python net_scan.py -t 192.168.1.1/24
```

### Verbose Scan

To perform a verbose scan of the network in the IP range `192.168.1.1/24`:

```sh
python net_scan.py -t 192.168.1.1/24 -v
```

## Troubleshooting

### Common Issues

1. **Permission Denied**:
   - Ensure you are running the script with administrative privileges. On Windows, right-click the Command Prompt and select "Run as administrator".
   
2. **Npcap not installed**:
   - Make sure Npcap is installed and configured correctly on Windows. Follow the steps in the [Installation](#installation) section.

3. **Scapy Import Error**:
   - Ensure Scapy is installed correctly. You can install it using `pip install scapy`.

### Reporting Issues

If you encounter any issues that are not addressed here, please open an issue on the [GitHub Issues](https://github.com/diaaatya/net_scan/issues) page.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Issues

If you encounter any issues or have questions, feel free to open an issue on the [GitHub Issues](https://github.com/yourusername/network-scanner/issues) page.

---

This user guide should help users install, configure, and use your network scanner tool effectively.
