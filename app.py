#! /usr/bin/python3
import os
from custom_modules.PasswordGenerator import generate_password_thread as gpt
from custom_modules.PlatformConstants import USER_DIR

# print("Password:\t{}".format(gpt()))

print("{}\n{}".format(USER_DIR, os.system("ls {}".format(USER_DIR))))
