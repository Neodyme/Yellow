import socket
from struct import *
import datetime
import pcap
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
    
        s.send("start")
        while(1) :
                packet = s.recv(1500)
                parse_packet(packet[16:])
		
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

def parse_TCP(packet, iph_length, eth_length, l):
	t = iph_length + eth_length
        tcp_header = packet[t:t+20]

        
        tcph = unpack('!HHLLBBHHH' , tcp_header)
        
        source_port = tcph[0]
        dest_port = tcph[1]
        sequence = tcph[2]
        acknowledgement = tcph[3]
        doff_reserved = tcph[4]
        tcph_length = doff_reserved >> 4
            
	#Adding TCP informations to the l
	l.append(str(source_port)) #src port
	l.append(str(dest_port)) #dest port
	l.append(str(sequence)) #Sequence Number
	l.append(str(acknowledgement)) #Acknowledgement
	l.append(str(tcph_length)) #TCP header length
             
        h_size = eth_length + iph_length + tcph_length * 4
        data_size = len(packet) - h_size
             
        data = packet[h_size:]
        l.append(data) #DATA

def parse_ICMP(packet, iph_length, eth_length, l):
	u = iph_length + eth_length
        icmph_length = 4
	icmp_header = packet[u:u+4]
 
        icmph = unpack('!BBH' , icmp_header)
             
        icmp_type = icmph[0]
        code = icmph[1]
        checksum = icmph[2]
    
	#Adding ICMP informations to the l
	l.append(str(icmp_type)) #TYPE
	l.append(str(code)) #Code
	l.append(str(checksum)) #Checksum
             
        h_size = eth_length + iph_length + icmph_length
        data_size = len(packet) - h_size
             
        data = packet[h_size:]
        l.append(data) #DATA         
 
def parse_UDP(packet, iph_length, eth_length, l):
	u = iph_length + eth_length
        udph_length = 8
        udp_header = packet[u:u+8]
 
        udph = unpack('!HHHH' , udp_header)
             
        source_port = udph[0]
        dest_port = udph[1]
        length = udph[2]
        checksum = udph[3]
	
    #Adding ICMP informations to the l
	l.append(str(source_port)) #SRC PORT
	l.append(str(dest_port)) #DEST PORT
	l.append(str(length)) #Length
	l.append(str(checksum)) #Checksum         
             
        h_size = eth_length + iph_length + udph_length
        data_size = len(packet) - h_size
             
        data = packet[h_size:]
        l.append(data) #DATA          

#function to parse a packet
def parse_packet(packet):

        print(len(packet))
        if(len(packet)) < 16:
                return
        l = []
        
        l.append("date")
        l.append("time")
	 
        eth_length = 14
        eth_header = packet[:eth_length]
        eth = unpack('!6s6sH' , eth_header)
        eth_protocol = socket.ntohs(eth[2])
	
	l.append(eth_addr(packet[0:6])) #dest MAC
	l.append(eth_addr(packet[6:12])) #src MAC

        
	#naming the protocole
	l.append(name_proto(eth_protocol))

        print(l)
        
        if eth_protocol == 8:
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
 
		#Adding HEADER informations to the l
        l.append(str(version)) #version
        l.append(str(ihl)) #IP Header Length
        l.append(str(ttl)) #TTL
        l.append(name_proto(protocol)) #protocol
        l.append(str(s_addr)) #src address
        l.append(str(d_addr)) #dest address
        
        if protocol == 6: #Protocol = 6 (TCP) 
                parse_TCP(packet, iph_length, eth_length, l)        
        elif protocol == 1: #Protocol = 1 (ICMP)
                parse_ICMP(packet, iph_length, eth_length, l)        
        elif protocol == 17: #Protocol = 1 (UDP)
                parse_UDP(packet, iph_length, eth_length, l)   
 
if __name__ == "__main__":
  main(sys.argv)
