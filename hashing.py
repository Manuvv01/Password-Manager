import bcrypt
import json
import time
import usb, password

with open("data.json", "r") as data_file:
    data = json.load(data_file)

key = data.get("link-start")


def verify(usb_driver):
    data_usb = usb.get_obj(usb_driver) #Gets the obj of the USB
    user_password = data_usb.get("key")

    key_b = key.encode()
    password_b = user_password.encode()

    print("Verifying Credentials....")
    time.sleep(2)

    if bcrypt.checkpw(password_b, key_b):
        print("Unlock")
        return True
    else:
        print("Lock")
        return False







# key_hashed = key.encode()
# password_b = password.encode()
#
# if bcrypt.checkpw(password_b, key_hashed):
#     print("Unlock")
# else:
#     print("Lock")



# if __name__ == "__main__":

