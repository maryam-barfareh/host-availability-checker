import os
import platform

target = input("Enter target IP or hostname: ")

print("Checking availability for:", target)

system = platform.system()

if system == "Windows":
    command = "ping -n 1 " + target
else:
    command = "ping -c 1 " + target

response = os.system(command)

if response == 0:
    print("Host is UP")
else:
    print("Host is DOWN")
