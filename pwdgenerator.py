#! /usr/bin/python3

import argparse
import os
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms

cus = cms["custom"]
msg = None
desc = "This program will generate a random string of characters"
epil = "The string is generated from a combination of digits, upper and lower case letters and punctuation characters"
vers = "%prog 0.1"
verbose = False
save_to_file = False


def error_handler(*args):
    cus = cms["custom"]
    arg = args[0]
    cargs = cus(254, 64, 4, arg)
    print("{}".format(cargs))
    os.system("exit")


parser = argparse.ArgumentParser(description=desc, epilog=epil)

parser.error = error_handler

parser.version = vers


""" group arguments  """

group = parser.add_mutually_exclusive_group()

group.add_argument(
    "-v",
    "--verbose",
    dest="verbose",
    action="store_true",
    help="Increase output verbosity",
)

""" positional arguments  """

parser.add_argument(
    "-g",
    "--generate",
    dest="generate",
    action="store_true",
    help="Generates a random string",
)

args = parser.parse_args()
