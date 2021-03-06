# -*- coding: utf-8 -*-

import getopt
import sys

from genome import GenomeReport


def main(argv):
    """Run program."""
    genome_file = False
    outputformat = 'html'
    help_text = '{} -g <genome_file.txt> -f <html,pdf>'.format(sys.argv[0])
    try:
        opts, args = getopt.getopt(argv, "g:f:", ["genome=", "format="])
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_text)
            sys.exit()
        elif opt in ("-g", "--genome"):
            genome_file = arg
        elif opt in ("-f", "--format"):
            arg = arg.lower()
            if arg in ['html', 'pdf']:
                outputformat = arg
            else:
                outputformat = 'html'
    if not genome_file:
        print('Error: {}'.format(help_text))
        sys.exit(2)
    genome_obj = GenomeReport(genome_file, report_format=outputformat)
    genome_obj.make_report()

if __name__ == "__main__":
    main(sys.argv[1:])
