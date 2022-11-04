#! /usr/bin/python3
import re
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.PlatformConstants import LINE_SEP as lsep
from custom_modules.PatternConstants import is_number_only as ino


cus = cms["custom"]


user_input = input("Enter something:\t")


m_header = cus(255, 222, 0, "You Entered:")
m_body = cus(255, 255, 255, "{}".format(user_input))
msg = "{} {}{}".format(m_header, m_body, lsep)


print("{}".format(msg))

status, data = ino(user_input)

if status:
    print("{}".format(data.span()))
    print("{}".format(data.string))
    print("{}".format(data.group()))
