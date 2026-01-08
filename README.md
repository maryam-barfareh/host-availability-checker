# Host Availability Checker

This project is a simple Python script that checks whether a host
(IP address or hostname) is reachable on the network.

The script uses the system `ping` command and works on both
Windows and Unix-based operating systems.

## How It Works

- The user enters a target IP address or hostname
- The script detects the operating system
- One ICMP ping request is sent to the target
- Based on the response code, the host is marked as UP or DOWN

## Requirements

- Python 3.x
- Network access
- Ping command available on the system

## Usage

Run the script from the terminal:

## EXAMPLT

Enter target IP or hostname: 8.8.8.8
Checking availability for: 8.8.8.8
Host is UP

```bash

python host_availability_checker.py
