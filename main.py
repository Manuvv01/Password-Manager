import time
import psutil #To access USB drives
import os
import json
import usb, password

if __name__  == "__main__":
    usb_info = usb.wait_for_usb()
    usb.check_usb_json(usb_info)
