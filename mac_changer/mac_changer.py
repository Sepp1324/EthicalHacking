#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's Mac-Adress")
parser.parse_args()

interface = raw_input("Interface: ")
new_mac = raw_input("New Mac-Adress: ")

print("[+] Changing Mac-Adress for interface " + interface)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] Changed Mac-Adress successfully to " + new_mac + "!")