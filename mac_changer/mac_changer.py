#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
	parser = optparse.OptionParser()

	parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's Mac-Adress")
	parser.add_option("-m", "--mac", dest="new_mac", help="New Mac-Adress")
	(options, arguments) = parser.parse_args()

	if not options.interface:
		parser.error("[-] You need to specify an interface! --help")

	elif not options.new_mac:
		parser.error("[-] You need to specify a Mac-Adress! --help")
	return options


def change_mac(interface, new_mac):
	print("[+] Changing Mac-Adress for interface " + interface)

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])	


def get_reg_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])

	mac_query = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

	if mac_query:
		return mac_query.group(0)
	else:
		print("[-] Could not read Mac-Address!")


curr_mac = get_reg_mac(get_arguments().interface)

print("Current Mac-Address: " + str(curr_mac))
