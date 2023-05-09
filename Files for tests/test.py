import hashlib

md5_hash_Password = hashlib.md5("2".encode()).hexdigest()
print(type(md5_hash_Password))
