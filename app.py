#! /usr/bin/python3

from custom_modules.ArgumentManager import filtered as args, filtered_count as argsc
from custom_modules.EncoderDecoder import encode, decode
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.Utils import exit_prog as exit

coder = {"encode": encode, "decode": decode}

if argsc == 2:    
    cus = cms['custom']
    data = args[0]
    action = args[1]
    
    try:
        method = coder[action]
        res = method(data)
        status = res['status']
        
        if status:
            print("\nAction: {}\nData: {}\nResults: {}\nType: {}\n".format(action,data,res['encoded'],type(res['encoded'])))
        else:
            e_msg_header = cus(255,100,100,"Error:")
            e_msg_body = cus(255,255,255,res['reason'])
            e_msg = "{} {}".format(e_msg_header,e_msg_body)
            print("{}".format(e_msg))
        
    except KeyError as ker:
        e_msg_header = cus(255,100,100,"Error:")
        e_msg_body = cus(255,255,255,"{} is not a valid command.".format(ker))
        e_msg = "{} {}".format(e_msg_header,e_msg_body)
        print("{}\n".format(e_msg))
    except Exception as exc:
        e_msg_header = cus(255,100,100,"Error:")
        e_msg_body = cus(255,255,255,"{}".format(exc))
        e_msg = "{} {}".format(e_msg_header,e_msg_body)
        print("{}\n".format(e_msg))        
    finally:
        exit()
