#! /usr/bin/python3

import argparse
from multiprocessing.dummy import current_process
import os
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.PlatformConstants import USER_DIR, LINE_SEP
from custom_modules.PasswordGenerator import generate_password_thread as gpt
from custom_modules.FileOperator import save_new_file as snf

cus = cms["custom"]
msg = None
desc = "This program will generate a random string of characters"
epil = "The string is generated from a combination of digits, upper and lower case letters and punctuation characters"
vers = "%prog 0.1"
pwd = ""
name = "generated-password.txt"
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

# Increase verbosity
group.add_argument(
    "-v",
    "--verbose",
    dest="verbose",
    action="store_true",
    help="Increase output verbosity",
)

""" positional arguments  """

parser.add_argument(
    "-s",
    "--save",
    action="store_true",
    help="Saves the generated password to file in the usrer's home directory",
)

parser.add_argument("-n", "--name", help="Name output file. Works with [s] option.")

# Run the program
parser.add_argument(
    "-g",
    "--generate",
    dest="generate",
    action="store_true",
    help="Generates a random string",
)

args = parser.parse_args()

if args.verbose:
    verbose = True

if args.save:
    save_to_file = True

if args.name:
    name = args.name

if args.generate:
    if verbose:
        msg = cus(255, 255, 255, "... Generating password")
        print("\t\t{}\n".format(msg))

        pwd = gpt()
        pwd_msg = cus(10, 255, 15, "Password Successfully Generated")
        msg = cus(255, 255, 255, pwd)

        print("{}:\t{}".format(pwd_msg, msg))

        if save_to_file:
            dest = "{}/{}".format(USER_DIR, name)
            snf(dest, pwd)
            pwd_msg = cus(10, 255, 15, "Password Successfully Saved At {}".format(dest))

            print("{}".format(pwd_msg))
    else:
        pwd = gpt()
        print("{}".format(cus(255, 255, 255, pwd)))

        if save_to_file:
            dest = "{}/{}".format(USER_DIR, name)
            snf(dest, pwd)
            pwd_msg = cus(10, 255, 15, "Password Successfully Saved At {}".format(dest))

            print("{}".format(pwd_msg))
