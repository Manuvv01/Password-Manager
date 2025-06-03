import time
import psutil #To access USB drives
import os
import json

def get_usb_drives():
    usb_drives = []
    # Get all disk partitions as a list of sdiskpart objects, each with attributes
    partitions = psutil.disk_partitions()
    for p in partitions:
        if 'removable' in p.opts: #Find the opts attribute if is removable
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

def get_obj(usb_drive):
    json_path = os.path.join(usb_drive, "data.json")
    with open(json_path, "r") as f:
        file_data = json.load(f)
    return file_data

def get_key(usb_drive):
    path = os.path.join(usb_drive, "apolo.txt")
    with open(path, "rb") as f:
        file_data = f.read()
    return file_data


