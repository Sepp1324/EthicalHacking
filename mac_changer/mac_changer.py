#!/usr/bin/env python

import subprocess

interface = "eth0"
new_mac = "00:11:22:33:44:77"

print("[+] Changing Mac-Adress for interface " + interface)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface +" hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface +" up", shell=True)

print("[+] Changed Mac-Adress successfully to " + new_mac + "!")