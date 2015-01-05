/*
** yellow.h for  in /home/pprost
** 
** Made by  Prost P.
** Login   <pprost@epitech.net>
** 
** Started on  Tue Dec 23 12:25:41 2014 Prost P.
// Last update Sun Jan  4 10:54:09 2015 Prost P.
*/

#ifndef __YELLOW_HH_
# define  __YELLOW_HH_

#include <string>
#include <tins/tins.h> 

#define YELLOW_DEFAULT_PORT 1337

class probe_args
{
public:
  std::string listen_addr;
  std::string tapping_iface;
  std::string log_file;
  unsigned short listen_port;
  int sockfd;
  Tins::PacketWriter *writer;
  int quit;
  
  probe_args() {
     listen_port = YELLOW_DEFAULT_PORT;
     listen_addr = "127.0.0.1";
     tapping_iface = "eth0";
     log_file = "dump.log";
     quit = 0;
  }
};


int stage1(probe_args &);

#endif
