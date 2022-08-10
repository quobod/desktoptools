import argparse
import os

cus = cms["custom"]
msg = None
desc = "This program will generate a QR code image from the given text"
epil = "Generates a two dimensional Quick Response (QR) code  pictograph from any kind of data (e.g. binary, alphanumeric, or Kanji symbols) etc. The QR pictograph will be saved in the user's home directory."
vers = "%prog 0.1"
data = None
name = None
file = None
verbose = False
is_file = False


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
