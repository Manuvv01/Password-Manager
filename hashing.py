import bcrypt
import json
import time
import usb, password

with open("data.json", "r") as data_file:
    data = json.load(data_file)

key = data.get("link-start")
data_id = data.get("cookie")

def verify(usb_driver):
    data_usb = usb.get_obj(usb_driver) #Gets the obj of the USB
    user_password = data_usb.get("key")
    user_id = data_usb.get("id")

    key_b = key.encode()
    password_b = user_password.encode()
    dataid_b = data_id.encode()
    user_id_b = user_id.encode()

    print("Verifying Credentials....")
    time.sleep(2)

    if bcrypt.checkpw(password_b, key_b) and bcrypt.checkpw(user_id_b, dataid_b):
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

