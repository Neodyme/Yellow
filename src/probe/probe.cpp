//
// probe.cpp for  in /home/pprost
// 
// Made by  Prost P.
// Login   <pprost@epitech.net>
// 
// Started on  Tue Dec 23 12:37:52 2014 Prost P.
// Last update Wed Dec 24 19:36:48 2014 Prost P.
//

#include <iostream>
#include <tins/tins.h>
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

#include "yellow.hh"


bool callback(const Tins::PDU &pdu)
{
  const Tins::IP &ip = pdu.rfind_pdu<Tins::IP>(); // Find the IP layer
  const Tins::TCP &tcp = pdu.rfind_pdu<Tins::TCP>(); // Find the TCP layer
  std::cout << ip.src_addr() << ':' << tcp.sport() << " -> "
	    << ip.dst_addr() << ':' << tcp.dport() << std::endl;
  return true;
}

static void	*stage2(void *args)
{
  int sockfd, newsockfd, portno;
  socklen_t clilen;
  char buffer[256];
  struct sockaddr_in serv_addr, cli_addr;
  int n;

  sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if (sockfd < 0)
    errx(-1, "ERROR opening socket");

  bzero((char *) &serv_addr, sizeof(serv_addr));
  serv_addr.sin_family = AF_INET;
  serv_addr.sin_addr.s_addr = inet_addr(((probe_args*)args)->listen_addr.c_str());
  serv_addr.sin_port = htons(((probe_args*)args)->listen_port);

  if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
    errx(-1, "ERROR on binding");
  
  listen(sockfd, 5);
  clilen = sizeof(cli_addr);
  newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);

  if (newsockfd < 0)
    errx(-1, "ERROR on accept");
  bzero(buffer,256);

  while ((n = read(newsockfd, buffer, 255)))
    {
      std::cout << buffer << std::endl;
    }

  
  n = write(newsockfd,"I got your message",18);

  close(newsockfd);
  close(sockfd);
  return NULL;
}


int stage1(probe_args &args)
{
  pthread_t thread;
  pthread_create(&thread, NULL, stage2, &args);

  Tins::Sniffer(args.tapping_iface).sniff_loop(callback);
  std::cout << "toto" << std::endl;
}
