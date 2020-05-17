#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
	parser = optparse.OptionParser()

	parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's Mac-Adress")
	parser.add_option("-m", "--mac", dest="new_mac", help="New Mac-Adress")
	return parser.parse_args()


def change_mac(interface, new_mac):
	print("[+] Changing Mac-Adress for interface " + interface)

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])	


(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)	

print("[+] Changed Mac-Adress successfully to " + options.new_mac + "!")