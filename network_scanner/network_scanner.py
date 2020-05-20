#!/usr/bin/env python

import scapy.all as scapy
import optparse


def get_arguments():
	parser = optparse.OptionParser()

	parser.add_option("-t", "--target", dest="target", help="Choose the Target-IP")
	(options, arguments) = parser.parse_args()

	if not options.target:
		parser.error("You need to specify a Target!")
	return options


def scan(ip):
	arp_req = scapy.ARP(pdst=ip)
	bc = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_bc = bc/arp_req
	anwsered = scapy.srp(arp_req_bc, timeout=1, verbose=False)[0]

	clients = []

	for anwser in anwsered:
		clients_dict = {"ip": anwser[1].psrc, "mac": anwser[1].hwsrc}
		clients.append(clients_dict)
	return clients


def print_result(results):
	print("IP\t\t\tMac-Adress\n" + "-" * 41)

	for client in results:
		print(client["ip"] + "\t\t" + client["mac"])

scan_res = scan(get_arguments().target) 
print_result(scan_res)
