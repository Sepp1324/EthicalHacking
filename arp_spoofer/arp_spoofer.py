#!/usr/bin/env python

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="10.0.0.162", hwdst="e4:a7:a0:44:42:01", psrc="10.0.0.138")

