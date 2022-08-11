from pickletools import read_bytes8
import sys
import codecs
import base64
from custom_modules.FileValidator import fileExists as fe, isFile as isf
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms

cus = cms["custom"]


def encode():
    str = input("Enter your input to encode:\t")
    str = codecs.encode(str.encode(), encoding="base64", errors="strict")

    msg = "{}".format(str)
    cmsg = cus(255, 255, 255, msg)
    s_msg = cus(34, 255, 34, "Success:")

    print("{}\t{}\n".format(s_msg, cmsg))
    return str


def decode():
    str = input("Enter your encoded input to decode:\t")
    str = read_bytes8(str)
    str = codecs.decode(str, errors="strict")

    msg = "{}".format(str)
    cmsg = cus(255, 255, 255, msg)
    s_msg = cus(34, 255, 34, "Success:")

    print("{}\t{}\n".format(s_msg, cmsg))
    return str
