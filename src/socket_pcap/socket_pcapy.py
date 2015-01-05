import pcapy
from impacket.ImpactDecoder import *

#dev = pcapy.findalldevs()
#print dev

dev = 'eth0'
max_bytes = 1024
promiscous = False
read_timeout = 100
pcap_filter = ''

cap = pcapy.open_live(dev, max_bytes, promiscous, read_timeout)
cap.setfilter(pcap_filter)

def recv_packet(hdr, data):
    packet = EthDecoder().decode(data)
    print packet

packet_limit = -1
cap.loop(packet_limit, recv_packet)
