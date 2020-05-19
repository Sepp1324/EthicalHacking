#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
	arp_req = scapy.ARP(pdst=ip)
	print(arp_req.summary())


scan("10.0.0.1/24")