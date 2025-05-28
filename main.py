import time
import psutil #To access USB drives
import password
import os
import json
import subprocess  # To open/run your software

def get_usb_drives():
    usb_drives = []
    partitions = psutil.disk_partitions()
    for p in partitions:
        if 'removable' in p.opts or 'cdrom' in p.opts:
            usb_drives.append(p.device)
    return usb_drives

def wait_for_usb():
    print("Waiting for USB...")
    while True:
        usb_drives = get_usb_drives()
        if usb_drives:
            print(f"USB detected: {usb_drives[0]}")
            return usb_drives[0]  # Return drive path
        time.sleep(1)

if __name__ == "__main__":
    wait_for_usb()
    password.main()