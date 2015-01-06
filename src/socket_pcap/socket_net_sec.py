import socket
from struct import *
import datetime
import pcapy
import sys
 
def main(argv):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error:
		print 'Failed to create socket'
		sys.exit()

	print 'Socket Created'

	#connecting socket
	s.connect(('127.0.0.1', 1337))
    
    #reading and parsing packets
    while(1) :
        s.recv(1024)
        parse_packet(packet)
		
	s.Close()
 
#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
    return b

def name_proto(proto):
	if proto == 1:
		return "ICMP";
	elif proto == 6:
		return "TCP";
	elif proto == 8:
		return "HEADER";
	elif proto == 17:
		return "UDP";
	else:
		return proto;

def parse_TCP(iph_length, eth_length):
	t = iph_length + eth_length
    tcp_header = packet[t:t+20]
 
    tcph = unpack('!HHLLBBHHH' , tcp_header)
             
    source_port = tcph[0]
    dest_port = tcph[1]
    sequence = tcph[2]
    acknowledgement = tcph[3]
    doff_reserved = tcph[4]
    tcph_length = doff_reserved >> 4
            
	#Adding TCP informations to the list
	list.append(str(source_port)) #src port
	list.append(str(dest_port)) #dest port
	list.append(str(sequence)) #Sequence Number
	list.append(str(acknowledgement)) #Acknowledgement
	list.append(str(tcph_length)) #TCP header length
             
    h_size = eth_length + iph_length + tcph_length * 4
    data_size = len(packet) - h_size
             
    #get data from the packet
    data = packet[h_size:]
    list.append(data) #DATA

def parse_ICMP(iph_length, eth_length):
	u = iph_length + eth_length
    icmph_length = 4
	icmp_header = packet[u:u+4]
 
    icmph = unpack('!BBH' , icmp_header)
             
    icmp_type = icmph[0]
    code = icmph[1]
    checksum = icmph[2]
    
	#Adding ICMP informations to the list
	list.append(str(icmp_type)) #TYPE
	list.append(str(code)) #Code
	list.append(str(checksum)) #Checksum
             
    h_size = eth_length + iph_length + icmph_length
    data_size = len(packet) - h_size
             
    #get data from the packet
    data = packet[h_size:]
    list.append(data) #DATA         
 
def parse_UDP(iph_length, eth_length):
	u = iph_length + eth_length
    udph_length = 8
    udp_header = packet[u:u+8]
 
    udph = unpack('!HHHH' , udp_header)
             
    source_port = udph[0]
    dest_port = udph[1]
    length = udph[2]
    checksum = udph[3]
	
    #Adding ICMP informations to the list
	list.append(str(source_port)) #SRC PORT
	list.append(str(dest_port)) #DEST PORT
	list.append(str(length)) #Length
	list.append(str(checksum)) #Checksum         
             
    h_size = eth_length + iph_length + udph_length
    data_size = len(packet) - h_size
             
    #get data from the packet
    data = packet[h_size:]
    list.append(data) #DATA          

#function to parse a packet
def parse_packet(packet):
     #adding date/time to list
	 list.append("date")
	 list.append("time")
	 
    #parse ethernet header
    eth_length = 14
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])
	
	#puting MAC informations in the list
	list.append(eth_addr(packet[0:6])) #dest MAC
	list.append(eth_addr(packet[6:12])) #src MAC
	
	#naming the protocole
	list.append(name_proto(eth_protocol))

    #Protocol = 8 (HEADER)
    if eth_protocol == 8:
		#IP Header Length
        ip_header = packet[eth_length:20+eth_length]
        iph = unpack('!BBHHHBBH4s4s' , ip_header)
 
		#verion
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
 
        iph_length = ihl * 4
		
		#getting informations
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8]);
        d_addr = socket.inet_ntoa(iph[9]);
 
		#Adding HEADER informations to the list
		list.append(str(version)) #version
		list.append(str(ihl)) #IP Header Length
		list.append(str(ttl)) #TTL
		list.append(name_proto(protocol)) #protocol
		list.append(str(s_addr)) #src address
		list.append(str(d_addr)) #dest address
        
        if protocol == 6: #Protocol = 6 (TCP) 
            parse_TCP(iph_length, eth_length)        
        elif protocol == 1: #Protocol = 1 (ICMP)
            parse_ICMP(iph_length, eth_length)        
        elif protocol == 17: #Protocol = 1 (UDP)
			parse_UDP(iph_length, eth_length)      
 
if __name__ == "__main__":
  main(sys.argv)
