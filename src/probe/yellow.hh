/*
** yellow.h for  in /home/pprost
** 
** Made by  Prost P.
** Login   <pprost@epitech.net>
** 
** Started on  Tue Dec 23 12:25:41 2014 Prost P.
// Last update Wed Dec 24 19:31:42 2014 Prost P.
*/

#ifndef __YELLOW_HH_
# define  __YELLOW_HH_

#include <string>

#define YELLOW_DEFAULT_PORT 1337


class probe_args
{
public:
  std::string listen_addr;
  std::string tapping_iface;
  int listen_port;

  probe_args() {
     listen_port = YELLOW_DEFAULT_PORT;
     listen_addr = "127.0.0.1";
     tapping_iface = "eth0";
  }
};


int stage1(probe_args &);

#endif
