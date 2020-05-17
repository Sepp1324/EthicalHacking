#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's Mac-Adress")
parser.add_option("-m", "--mac", dest="new_mac", help="New Mac-Adress")

(options, arguments) = parser.parse_args()

interface = options.interface 
new_mac = options.new_mac 

print("[+] Changing Mac-Adress for interface " + interface)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] Changed Mac-Adress successfully to " + new_mac + "!")