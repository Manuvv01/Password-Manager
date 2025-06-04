from cryptography.fernet import Fernet
import json
# OPEN KEY IN USB
access_key = b"VNTV08oQcxuwDcKbuRDVdOa6v6LzaORKGOg7E3357Z8="
# DECRYPT
f = Fernet(access_key)
# READ
with open("stargate.json", "rb") as x:
    encrypt_file = x.read()

decrypt_file = f.decrypt(encrypt_file)

with open("huh.json", "wb") as a:
    a.write(decrypt_file)

with open("huh.json", "r") as y:
    data = json.load(y)

key = data.get("link-start")
data_id = data.get("cookie")
name = data.get("owner")

print(f"Name: {name}/Key:{key}/ID:{data_id}")




