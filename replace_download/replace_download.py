#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())

	if scapy_packet.haslayer(scapy.Raw):
		if scapy_packet[scapy.TCP].dport == 80:
			print("HTTP Request: ")
			if ".exe" in scapy_packet[scapy.Raw].load:
				print("[+] .exe Request")
				print(scapy_packet.show())
		elif scapy_packet[scapy.TCP].sport == 80:
			print("HTTP Resolve: ")
			print(scapy_packet.show())
	packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet) # Callback-Function
queue.run()
