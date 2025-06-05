from os import access
import bcrypt
from cryptography.fernet import Fernet
import json, time
import usb


def verify(usb_driver):

    def decr():
        # OPEN KEY IN USB
        access_key = usb.get_key()
        # DECRYPT
        f = Fernet(access_key)
        # READ
        with open("stargate.json", "rb") as x:
            encrypt_file = x.read()

        decrypt_file = f.decrypt(encrypt_file)

        with open("huh.json", "wb") as a:
            a.write(decrypt_file)

    decr()

    with open("huh.json", "r") as data_file:
        data = json.load(data_file)

    key = data.get("link-start")
    data_id = data.get("cookie")
    name = data.get("owner")

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


