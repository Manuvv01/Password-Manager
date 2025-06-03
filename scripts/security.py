import bcrypt
import json, time
import usb

with open("data.json", "r") as data_file:
    data = json.load(data_file)

key = data.get("link-start")
data_id = data.get("cookie")
name = data.get("owner")

def verify(usb_driver):

    #USB DATA
    data_usb = usb.get_obj(usb_driver) #obj
    user_password = data_usb.get("key")
    user_id = data_usb.get("id")
    name_usb = data_usb.get("owner")

    #ENCODING
    key_b = key.encode()
    password_b = user_password.encode()
    dataid_b = data_id.encode()
    user_id_b = user_id.encode()

    print("Verifying Credentials....")
    time.sleep(2)

    if bcrypt.checkpw(password_b, key_b) and bcrypt.checkpw(user_id_b, dataid_b) and name == name_usb:
        print("Unlock")
        return True
    else:
        print("Lock")
        return False

# def encr(usb_driver):
#     mstr_key = usb.get_key(usb_driver)