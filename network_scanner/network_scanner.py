#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
	arp_req = scapy.ARP(pdst=ip)
	bc = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_bc = bc/arp_req
	anwsered = scapy.srp(arp_req_bc, timeout=1, verbose=False)[0]

	print("IP\t\t\tMac-Adress")
	print("-" * 41)

	for anwser in anwsered:
		print(anwser[1].psrc + "\t\t" + anwser[1].hwsrc)


scan("10.0.0.138/24") 