from scapy.all import *
from collections import Counter
s = str()
packet_counts=Counter()

def action(packet=None):
    global s
    if packet:
            
        key=tuple(sorted([packet[0][0].src, packet[0][0].dst]))
        if packet[0][0].src=='f8:63:3f:e0:6f:91' or  packet[0][0].dst=='f8:63:3f:e0:6f:91':
            s=packet[0][1].summary()
            packet_counts.update([key])



sniff(filter="ip", prn=action, count=1)


