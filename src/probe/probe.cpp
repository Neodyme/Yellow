//
// probe.cpp for  in /home/pprost
// 
// Made by  Prost P.
// Login   <pprost@epitech.net>
// 
// Started on  Tue Dec 23 12:37:52 2014 Prost P.
// Last update Thu Jan  8 11:23:43 2015 Prost P.
//

#include <iostream>

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <err.h>

#include<netinet/in.h>
#include<errno.h>
#include<netdb.h>
#include<stdio.h> //For standard things
#include<stdlib.h>    //malloc
#include<string.h>    //strlen

#include<netinet/ip_icmp.h>   //Provides declarations for icmp header
#include<netinet/udp.h>   //Provides declarations for udp header
#include<netinet/tcp.h>   //Provides declarations for tcp header
#include<netinet/ip.h>    //Provides declarations for ip header
#include<netinet/if_ether.h>  //For ETH_P_ALL
#include<net/ethernet.h>  //For ether_header
#include<sys/socket.h>
#include<arpa/inet.h>
#include <net/if.h>

#include <linux/if_packet.h>
#include <linux/if_ether.h>

#include<sys/ioctl.h>
#include<sys/time.h>
#include<sys/types.h>
#include<unistd.h>

void ProcessPacket(unsigned char* , int);
void print_ip_header(unsigned char* , int);
void print_tcp_packet(unsigned char * , int );
void print_udp_packet(unsigned char * , int );
void print_icmp_packet(unsigned char* , int );
void PrintData (unsigned char* , int);

#include <pcap/pcap.h>

#include "yellow.hh"

static probe_args *a;

FILE *logfile;
struct sockaddr_in source,dest;
int tcp=0, udp=0, icmp=0, others=0, igmp=0, total=0,i,j;


void ProcessPacket(unsigned char* buffer, int size)
{
  //Get the IP Header part of this packet , excluding the ethernet header
  struct iphdr *iph = (struct iphdr*)(buffer + sizeof(struct ethhdr));
  ++total;
  switch (iph->protocol) //Check the Protocol and do accordingly...
    {
    case 1:  //ICMP Protocol
      ++icmp;
      print_icmp_packet( buffer , size);
      break;

    case 2:  //IGMP Protocol
      ++igmp;
      break;

    case 6:  //TCP Protocol
      ++tcp;
      print_tcp_packet(buffer , size);
      break;

    case 17: //UDP Protocol
      ++udp;
      print_udp_packet(buffer , size);
      break;

    default: //Some Other Protocol like ARP etc.
      ++others;
      break;
    }
  printf("TCP : %d   UDP : %d   ICMP : %d   IGMP : %d   Others : %d   Total : %d\r", tcp , udp , icmp , igmp , others , total);
}

void print_ethernet_header(unsigned char* Buffer, int Size)
{
  struct ethhdr *eth = (struct ethhdr *)Buffer;

  fprintf(logfile , "\n");
  fprintf(logfile , "Ethernet Header\n");
  fprintf(logfile , "   |-Destination Address : %.2X-%.2X-%.2X-%.2X-%.2X-%.2X \n", eth->h_dest[0] , eth->h_dest[1] , eth->h_dest[2] , eth->h_dest[3] , eth->h_dest[4] , eth->h_dest[5] );
  fprintf(logfile , "   |-Source Address      : %.2X-%.2X-%.2X-%.2X-%.2X-%.2X \n", eth->h_source[0] , eth->h_source[1] , eth->h_source[2] , eth->h_source[3] , eth->h_source[4] , eth->h_source[5] );
  fprintf(logfile , "   |-Protocol            : %u \n",(unsigned short)eth->h_proto);
}

void print_ip_header(unsigned char* Buffer, int Size)
{
  unsigned short iphdrlen;

  print_ethernet_header(Buffer , Size);
  
  struct iphdr *iph = (struct iphdr *)(Buffer  + sizeof(struct ethhdr) );
  iphdrlen =iph->ihl*4;

  memset(&source, 0, sizeof(source));
  source.sin_addr.s_addr = iph->saddr;

  memset(&dest, 0, sizeof(dest));
  dest.sin_addr.s_addr = iph->daddr;

  fprintf(logfile , "\n");
  fprintf(logfile , "IP Header\n");
  fprintf(logfile , "   |-IP Version        : %d\n",(unsigned int)iph->version);
  fprintf(logfile , "   |-IP Header Length  : %d DWORDS or %d Bytes\n",(unsigned int)iph->ihl,((unsigned int)(iph->ihl))*4);
  fprintf(logfile , "   |-Type Of Service   : %d\n",(unsigned int)iph->tos);
  fprintf(logfile , "   |-IP Total Length   : %d  Bytes(Size of Packet)\n",ntohs(iph->tot_len));
  fprintf(logfile , "   |-Identification    : %d\n",ntohs(iph->id));
  //fprintf(logfile , "   |-Reserved ZERO Field   : %d\n",(unsigned int)iphdr->ip_reserved_zero);
  //fprintf(logfile , "   |-Dont Fragment Field   : %d\n",(unsigned int)iphdr->ip_dont_fragment);
  //fprintf(logfile , "   |-More Fragment Field   : %d\n",(unsigned int)iphdr->ip_more_fragment);
  fprintf(logfile , "   |-TTL      : %d\n",(unsigned int)iph->ttl);
  fprintf(logfile , "   |-Protocol : %d\n",(unsigned int)iph->protocol);
  fprintf(logfile , "   |-Checksum : %d\n",ntohs(iph->check));
  fprintf(logfile , "   |-Source IP        : %s\n",inet_ntoa(source.sin_addr));
  fprintf(logfile , "   |-Destination IP   : %s\n",inet_ntoa(dest.sin_addr));
}

void print_tcp_packet(unsigned char* Buffer, int Size)
{
  unsigned short iphdrlen;

  struct iphdr *iph = (struct iphdr *)( Buffer  + sizeof(struct ethhdr) );
  iphdrlen = iph->ihl*4;

  struct tcphdr *tcph=(struct tcphdr*)(Buffer + iphdrlen + sizeof(struct ethhdr));

  int header_size =  sizeof(struct ethhdr) + iphdrlen + tcph->doff*4;

  fprintf(logfile , "\n\n***********************TCP Packet*************************\n");

  print_ip_header(Buffer,Size);

  fprintf(logfile , "\n");
  fprintf(logfile , "TCP Header\n");
  fprintf(logfile , "   |-Source Port      : %u\n",ntohs(tcph->source));
  fprintf(logfile , "   |-Destination Port : %u\n",ntohs(tcph->dest));
  fprintf(logfile , "   |-Sequence Number    : %u\n",ntohl(tcph->seq));
  fprintf(logfile , "   |-Acknowledge Number : %u\n",ntohl(tcph->ack_seq));
  fprintf(logfile , "   |-Header Length      : %d DWORDS or %d BYTES\n" ,(unsigned int)tcph->doff,(unsigned int)tcph->doff*4);
  //fprintf(logfile , "   |-CWR Flag : %d\n",(unsigned int)tcph->cwr);
  //fprintf(logfile , "   |-ECN Flag : %d\n",(unsigned int)tcph->ece);
  fprintf(logfile , "   |-Urgent Flag          : %d\n",(unsigned int)tcph->urg);
  fprintf(logfile , "   |-Acknowledgement Flag : %d\n",(unsigned int)tcph->ack);
  fprintf(logfile , "   |-Push Flag            : %d\n",(unsigned int)tcph->psh);
  fprintf(logfile , "   |-Reset Flag           : %d\n",(unsigned int)tcph->rst);
  fprintf(logfile , "   |-Synchronise Flag     : %d\n",(unsigned int)tcph->syn);
  fprintf(logfile , "   |-Finish Flag          : %d\n",(unsigned int)tcph->fin);
  fprintf(logfile , "   |-Window         : %d\n",ntohs(tcph->window));
  fprintf(logfile , "   |-Checksum       : %d\n",ntohs(tcph->check));
  fprintf(logfile , "   |-Urgent Pointer : %d\n",tcph->urg_ptr);
  fprintf(logfile , "\n");
  fprintf(logfile , "                        DATA Dump                         ");
  fprintf(logfile , "\n");

  fprintf(logfile , "IP Header\n");
  PrintData(Buffer,iphdrlen);

  fprintf(logfile , "TCP Header\n");
  PrintData(Buffer+iphdrlen,tcph->doff*4);

  fprintf(logfile , "Data Payload\n");
  PrintData(Buffer + header_size , Size - header_size );

  fprintf(logfile , "\n###########################################################");
}

void print_udp_packet(unsigned char *Buffer , int Size)
{

  unsigned short iphdrlen;

  struct iphdr *iph = (struct iphdr *)(Buffer +  sizeof(struct ethhdr));
  iphdrlen = iph->ihl*4;

  struct udphdr *udph = (struct udphdr*)(Buffer + iphdrlen  + sizeof(struct ethhdr));

  int header_size =  sizeof(struct ethhdr) + iphdrlen + sizeof udph;

  fprintf(logfile , "\n\n***********************UDP Packet*************************\n");

  print_ip_header(Buffer,Size);

  fprintf(logfile , "\nUDP Header\n");
  fprintf(logfile , "   |-Source Port      : %d\n" , ntohs(udph->source));
  fprintf(logfile , "   |-Destination Port : %d\n" , ntohs(udph->dest));
  fprintf(logfile , "   |-UDP Length       : %d\n" , ntohs(udph->len));
  fprintf(logfile , "   |-UDP Checksum     : %d\n" , ntohs(udph->check));

  fprintf(logfile , "\n");
  fprintf(logfile , "IP Header\n");
  PrintData(Buffer , iphdrlen);

  fprintf(logfile , "UDP Header\n");
  PrintData(Buffer+iphdrlen , sizeof udph);

  fprintf(logfile , "Data Payload\n");

  //Move the pointer ahead and reduce the size of string
  PrintData(Buffer + header_size , Size - header_size);

  fprintf(logfile , "\n###########################################################");
}

void print_icmp_packet(unsigned char* Buffer , int Size)
{
  unsigned short iphdrlen;

  struct iphdr *iph = (struct iphdr *)(Buffer  + sizeof(struct ethhdr));
  iphdrlen = iph->ihl * 4;

  struct icmphdr *icmph = (struct icmphdr *)(Buffer + iphdrlen  + sizeof(struct ethhdr));

  int header_size =  sizeof(struct ethhdr) + iphdrlen + sizeof icmph;

  fprintf(logfile , "\n\n***********************ICMP Packet*************************\n");

  print_ip_header(Buffer , Size);

  fprintf(logfile , "\n");

  fprintf(logfile , "ICMP Header\n");
  fprintf(logfile , "   |-Type : %d",(unsigned int)(icmph->type));

  if((unsigned int)(icmph->type) == 11)
    {
      fprintf(logfile , "  (TTL Expired)\n");
    }
  else if((unsigned int)(icmph->type) == ICMP_ECHOREPLY)
    {
      fprintf(logfile , "  (ICMP Echo Reply)\n");
    }

  fprintf(logfile , "   |-Code : %d\n",(unsigned int)(icmph->code));
  fprintf(logfile , "   |-Checksum : %d\n",ntohs(icmph->checksum));
  //fprintf(logfile , "   |-ID       : %d\n",ntohs(icmph->id));
  //fprintf(logfile , "   |-Sequence : %d\n",ntohs(icmph->sequence));
  fprintf(logfile , "\n");

  fprintf(logfile , "IP Header\n");
  PrintData(Buffer,iphdrlen);

  fprintf(logfile , "UDP Header\n");
  PrintData(Buffer + iphdrlen , sizeof icmph);

  fprintf(logfile , "Data Payload\n");

  //Move the pointer ahead and reduce the size of string
  PrintData(Buffer + header_size , (Size - header_size) );

  fprintf(logfile , "\n###########################################################");
}

void PrintData (unsigned char* data , int Size)
{
  int i , j;

  for(i=0 ; i < Size ; i++)
    {
      if( i!=0 && i%16==0)   //if one line of hex printing is complete...
	{
	  fprintf(logfile , "         ");
	  for(j=i-16 ; j<i ; j++)
	    {
	      if(data[j]>=32 && data[j]<=128)
		fprintf(logfile , "%c",(unsigned char)data[j]); //if its a number or alphabet

	      else fprintf(logfile , "."); //otherwise print a dot
	    }
	  fprintf(logfile , "\n");
	}

      if(i%16==0) fprintf(logfile , "   ");
      fprintf(logfile , " %02X",(unsigned int)data[i]);

      if( i==Size-1)  //print the last spaces
	{
	  for(j=0;j<15-i%16;j++)
	    {
	      fprintf(logfile , "   "); //extra spaces
	    }

	  fprintf(logfile , "         ");

	  for(j=i-i%16 ; j<=i ; j++)
	    {
	      if(data[j]>=32 && data[j]<=128)
		{
		  fprintf(logfile , "%c",(unsigned char)data[j]);
		}
	      else
		{
		  fprintf(logfile , ".");
		}
	    }

	  fprintf(logfile ,  "\n" );
	}
    }
}


struct pcap_pkthdr_legacy

{
  bpf_u_int32 ts; /* time stamp */
  bpf_u_int32 tsu; /* time stamp */
  bpf_u_int32 caplen; /* length of portion present */
  bpf_u_int32 len; /* length this packet (off wire) */
};

void *stage25(void *args)
{
  int saddr_size , data_size;
  struct sockaddr saddr;
  struct pcap_file_header  header;
  struct pcap_pkthdr_legacy pkthdr;
  struct sockaddr_ll sll;
 
  struct ifreq ifr;
  
  struct timeval tv;
  clock_t timestamp;

  header.magic = ntohl(0xa1b2c3d4);
  header.version_major = 2;
  header.version_minor = 4;
  header.thiszone =  0;       /* GMT to local correction */
  header.sigfigs = 0;       /* accuracy of timestamps */
  header.snaplen = ntohs(65535);        /* max length of captured packets, in octets */
  header.linktype = ntohl(DLT_EN10MB);        /* data link type */
    
  unsigned char *buffer = (unsigned char *) malloc(65536); //Its Big!

  printf("Dumping log in: %s\n", ((probe_args*)args)->log_file.c_str());
  logfile = fopen(((probe_args*)args)->log_file.c_str(), "w");

  if(logfile==NULL)
    {
      printf("Unable to create log.txt file.");
    }
  printf("Starting...\n");

  timestamp = clock();
  
  int sock_raw = socket( AF_PACKET , SOCK_RAW , htons(ETH_P_ALL)) ;

  ((probe_args*)args)->sock_raw = sock_raw;

  printf("%d %d\n", sock_raw, ((probe_args*)args)->sock_raw);
  
  bzero(&ifr , sizeof(struct ifreq ));
  /* First Get the Interface Index */

  strncpy((char *) ifr.ifr_name , ((probe_args*)args)->tapping_iface.c_str(), IFNAMSIZ);
  if ((ioctl(sock_raw , SIOCGIFINDEX , & ifr )) == - 1)
    {
      printf("invalid interface: %s\n", ((probe_args*)args)->tapping_iface.c_str());
      exit(-1);
    }
  
  /* Bind our raw socket to this interface */
  sll.sll_family = AF_PACKET;
  sll.sll_ifindex = ifr.ifr_ifindex;
  sll.sll_protocol = htons(ETH_P_ALL);

  if((bind(sock_raw, (struct sockaddr *)&sll, sizeof(sll)))== -1)
    {
      perror("bind");
      return NULL;
    }
   

  // setsockopt(sock_raw,
  // 	     SOL_SOCKET,
  // 	     SO_BINDTODEVICE,
  // 	     "wlan0",
  // 	     5);

  send(((probe_args*)args)->sockfd, (char*)&header, sizeof (header), 0);

  if(sock_raw < 0)
    {
      //Print the error with proper message
      perror("Socket Error");
      pthread_exit(NULL);
      return NULL;
    }
  while(!((probe_args*)args)->quit)
    {
      saddr_size = sizeof saddr;
      //Receive a packet
      data_size = recvfrom(sock_raw , buffer + sizeof (struct pcap_pkthdr_legacy) , 65536 , 0 , &saddr , (socklen_t*)&saddr_size);

      if ((((struct iphdr*)(buffer + sizeof(struct ethhdr)))->protocol == 6) and
      	  (((struct tcphdr*)(buffer + ((struct iphdr *)(buffer  + sizeof(struct ethhdr)))->ihl * 4
      			     + sizeof(struct ethhdr)))->source == htons(1337)))
      	{
      	  printf("nok\n");
      	  continue;
      	}

      gettimeofday(&tv, NULL);

      ((struct pcap_pkthdr_legacy*)buffer)->ts = htonl(tv.tv_sec);
      ((struct pcap_pkthdr_legacy*)buffer)->tsu = htonl(tv.tv_usec);
      ((struct pcap_pkthdr_legacy*)buffer)->caplen = ntohl(data_size);
      ((struct pcap_pkthdr_legacy*)buffer)->len =  ntohl(data_size);
      send(((probe_args*)args)->sockfd, buffer, sizeof (struct pcap_pkthdr_legacy) + data_size, 0);

      if(data_size <0 )
	{
	  printf("Recvfrom error , failed to get packets\n");
	  pthread_exit(NULL);
	  return NULL;
	}
      //Now process the packet
      ProcessPacket(buffer + sizeof (struct pcap_pkthdr_legacy) , data_size);
    }
  close(sock_raw);
  printf("Stopping...");

  free(buffer);

  ((probe_args*)args)->quit = 0;
  pthread_exit(NULL);


  return NULL; 
}


void	inject(char *buffer, int len, probe_args *args)
{
  struct ethhdr *eth = (struct ethhdr *)(buffer + 6);
  struct sockaddr_ll socket_address;
  struct ifreq if_idx;

  memset(&if_idx, 0, sizeof(struct ifreq));
  
    /* Index of the network device */
  memcpy(socket_address.sll_addr, eth->h_dest, 6);
  /* Send packet */
  strncpy(if_idx.ifr_name, args->tapping_iface.c_str(), args->tapping_iface.length() - 1);
  if (ioctl(args->sock_raw, SIOCGIFINDEX, &if_idx) < 0)
    perror("SIOCGIFINDEX");
  
  if (sendto(args->sock_raw, buffer, len, 0, (struct sockaddr*)&socket_address, sizeof(struct sockaddr_ll)) < 0)
    perror("send");
  printf("   |-Destination Address : %.2X-%.2X-%.2X-%.2X-%.2X-%.2X \n",
	 eth->h_dest[0] , eth->h_dest[1] , eth->h_dest[2] , eth->h_dest[3] , eth->h_dest[4] , eth->h_dest[5] );


  
  std::cout << "Sending " << len << "bytes" << std::endl;  
}
	    
int	stage1(probe_args &args)
{
  pthread_t thread;
  int sockfd, newsockfd, portno;
  socklen_t clilen;
  char buffer[2560];
  struct sockaddr_in serv_addr, cli_addr;
  int n;

  a = &args;

  int z;     /* Status code */
  int so_reuseaddr = 1;

  sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if (sockfd < 0)
    errx(-1, "ERROR opening socket");

  z = setsockopt(sockfd, SOL_SOCKET,SO_REUSEADDR,
		 &so_reuseaddr,
		 sizeof so_reuseaddr);
  
  bzero((char *) &serv_addr, sizeof(serv_addr));
  serv_addr.sin_family = AF_INET;
  serv_addr.sin_addr.s_addr = inet_addr(args.listen_addr.c_str());
  serv_addr.sin_port = htons(args.listen_port);

  if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
    errx(-1, "ERROR on binding");
  
  listen(sockfd, 5);
  clilen = sizeof(cli_addr);

  while (1)
    {
      args.sockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
      
      if (args.sockfd < 0)
	errx(-1, "ERROR on accept");
      bzero(buffer,2560);

      while ((n = read(args.sockfd, buffer, 2550)))
	{
	  std::cout << buffer << std::endl;
	  if (strncasecmp(buffer, "START", 5) == 0)
	    {
	      pthread_create(&thread, NULL, stage25, &args);
	    }
	    if (strncasecmp(buffer, "STOP", 4) == 0)
	    {
	      args.quit = 1;
	      std::cout << "stoping" << std::endl;
	    }
	    if (strncasecmp(buffer, "INJECT", 6) == 0)
	      {

		struct ethhdr *eth = (struct ethhdr *)(buffer + 6);
		printf("   |-Destination Address : %.2X-%.2X-%.2X-%.2X-%.2X-%.2X \n",
		       eth->h_dest[0] , eth->h_dest[1] , eth->h_dest[2] , eth->h_dest[3] , eth->h_dest[4] , eth->h_dest[5] );
		printf("   |-Source Address      : %.2X-%.2X-%.2X-%.2X-%.2X-%.2X \n",
		       eth->h_source[0] , eth->h_source[1] , eth->h_source[2] , eth->h_source[3] , eth->h_source[4] , eth->h_source[5] );
		printf("   |-Protocol            : %u \n",(unsigned short)eth->h_proto);
		inject(buffer + 6, n - 6,  &args);
	    }

	}
    }
  std::cout << "exit stage 1" << std::endl;
  close(args.sockfd);
  close(sockfd);
}
