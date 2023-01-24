import hashlib

def md5_hash(filename):
    with open(filename,"rb")as f:
        bytes = f.read()
        md5hash = hashlib.md5(bytes).hexdigest()
        f.close()
    return md5hash

#print(md5_hash("Images\\784p9o.webp"))


def malware_checker(PathOfFile):
    hash_malware_check = md5_hash(PathOfFile)
    malware_hashes = open("virushash.txt")
    malware_hashes_read = malware_hashes.read()
    malware_hashes.close()
    print(malware_hashes_read)

malware_checker("Images\\784p9o.webp")