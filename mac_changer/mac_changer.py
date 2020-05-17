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


options = get_arguments()
#change_mac(options.interface, options.new_mac)	


#print("[+] Changed Mac-Adress successfully to " + options.new_mac + "!")

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])

#print(ifconfig_result)

mac_query = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

if mac_query:
	print("Successfully changed Mac-Address to: " + mac_query.group(0))
