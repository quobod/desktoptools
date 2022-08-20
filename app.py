#! /usr/bin/python3

from custom_modules.ArgumentManager import filtered, filtered_count
from custom_modules.EncoderDecoder import encode, decode

coder = {"encode": encode, "decode": decode}

if filtered_count == 1:
    action = filtered[0]
    f = coder[action]
    f()
