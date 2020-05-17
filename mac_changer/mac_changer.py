#!/usr/bin/env python

import subprocess

interface = raw_input("Interface: ")
new_mac = raw_input("New Mac-Adress: ")

print("[+] Changing Mac-Adress for interface " + interface)

#subprocess.call("ifconfig " + interface + " down", shell=True)
#subprocess.call("ifconfig " + interface +" hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface +" up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] Changed Mac-Adress successfully to " + new_mac + "!")