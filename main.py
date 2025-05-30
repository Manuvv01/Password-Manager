import time
import psutil #To access USB drives
import os
import json
import usb, password, hashing

if __name__  == "__main__":
    usb_info = usb.wait_for_usb()
    
    if hashing.verify(usb_info):
        password.main()
    else:
        print("Error")
