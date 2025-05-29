import time
import psutil #To access USB drives
import password
import os
import json
import subprocess  # To open/run your software

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

##Function to debug
def check_usb_json(usb_drive):
    json_path = os.path.join(usb_drive, "data.json")
    with open(json_path, "r") as data_file:
        data = json.load(data_file) #returns obj
        input_key = data.get("key")

    with open("data.json", "r") as f:
        sys_data = json.load(f)
        sys_key = sys_data.get("key")

    print("Verifying Credentials....")
    time.sleep(2)

    if input_key == sys_key:
        password.main()


