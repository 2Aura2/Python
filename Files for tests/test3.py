from Crypto.PublicKey import RSA
import os
# secret_code = "Unguessable"
# key = RSA.generate(2048)
# encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,protection="scryptAndAES128-CBC")

# file_out = open("rsa_key.bin","wb")
# file_out.write(encrypted_key)
# file_out.close()

# #print(key.publickey().export_key())


# encrypted_key2 = open("rsa_key.bin", "rb").read()
# key2 = RSA.import_key(encrypted_key2, passphrase=secret_code)
# print(key2.publickey().export_key())

# key = RSA.generate(2048)
# private_key = key.export_key()
# file_out = open("private.pem", "wb")
# file_out.write(private_key)
# file_out.close()

# public_key = key.publickey().export_key()
# file_out = open("receiver.pem","wb")
# file_out.write(public_key)
# file_out.close()

# filename = "rsa_key.bin"

# if os.path.isfile(filename):
#     print(f"The file {filename} exists.")
# else:
#     print(f"The file {filename} does not exist.")
