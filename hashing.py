import bcrypt

import usb

# password = b"DontHackMe"
# hash_password = "$2b$12$dG774NX0n.nUuvu89ajZPeFNbnFoqJRv6EmdR6hzPMU2OIDHU4h5y"
#
# hash_pass = bcrypt.hashpw(password, bcrypt.gensalt())
# hash_str=hash_pass.decode()
#
# ##Compare
#
# input_password = b"DontHackMe"
# store_hash = hash_str.encode()
#
# if bcrypt.checkpw(input_password, store_hash):
#     print("Match")
# else:
#     print("Incorrect")

if __name__ == "__main__":
    object_info= usb.get_obj()
    print(object_info)

