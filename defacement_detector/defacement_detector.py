#!/usr/bin/env python3

"""
    Main script from the project.
    Join crawler and values table scripts
"""

from pathlib import Path
from argparse import ArgumentParser

# Path from project's root
root_path = Path(__file__).parent.absolute().parent.absolute()

##### Arguments to the script #####

parser  = ArgumentParser()
parser.add_argument('-f', '--config_file', type=str, default=None
    help="Archivo de configuracion para el crawler")
parser.add_argument()

###################################

def get_output_file(infile):
    print(infile)

main():
    global parser
    get_output_file(parser.config_file)

if __name__ == "__main__":
    main()
