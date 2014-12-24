//
// main.cpp<probe> for  in /home/pprost
// 
// Made by  Prost P.
// Login   <pprost@epitech.net>
// 
// Started on  Tue Dec 23 11:51:04 2014 Prost P.
// Last update Wed Dec 24 11:40:40 2014 Prost P.
//

#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include "yellow.hh"

void	show_usage(char const *argv)
{
  dprintf(2, "Usage: %s  [OPTION...] -i INTERFACE\n\
Sniff to specified interface and dump network content in specified file or socket\n\n\
  -l Listening address.  default, sent content is not resent in socket\n\
  -p Listening Port. By default, port is 1337\n\
  -f File to dump data in\n",  argv);
  return;
}

int	main(int argc, char *argv[])
{
  char  c;
  probe_args args;

  while ((c = getopt (argc, argv, "l:p:f:i:")) != -1)
    switch (c)
      {
      case 'l':
	args.listen_addr = optarg;
	break;
      case 'i':
	args.tapping_iface = optarg;
	break;
      case '?':
	if (optopt == 'l')
	  fprintf (stderr, "Option -%c requires an argument.\n", optopt);
	else if (isprint (optopt))
	  fprintf (stderr, "Unknown option `-%c'.\n", optopt);
	else
	  fprintf (stderr, "Unknown option character `\\x%x'.\n",  optopt);
	return 1;
      default:
	show_usage(argv[0]);
      }
  if (optind != NULL)
    stage1(args);
  else
    show_usage(argv[0]);
  return (EXIT_SUCCESS);
}
