import hashlib

def md5_hash(filename):
    with open(filename,"rb")as f:
        bytes = f.read()
        md5hash = hashlib.md5(bytes).hexdigest()
        f.close()
    return md5hash


#print(md5_hash("Images\\Anti_Virus_BG.jpg"))
#print(md5_hash("Images\\Background.jpg"))
#print(md5_hash("Images\\Settings Button.png"))
#print(md5_hash("Images\\thumb-1920-77840.jpg"))


def malware_checker(PathOfFile):
    hash_malware_check = md5_hash(PathOfFile)
    
    malware_hashes = open("Files for tests\\virushash.txt","r")
    malware_hashes_read = malware_hashes.read()
    malware_hashes.close()
    
    virusinfo = open("Files for tests\\virusinfo.txt","r").readlines()
    
    if malware_hashes_read.find(hash_malware_check) != -1:
        #return virusinfo[malware_hashes_read.index(hash_malware_check)]
        print(virusinfo.index(str(malware_hashes_read.index(hash_malware_check))))
    else:
        return 0
    

print(malware_checker("Files for tests\\virusinfo.txt"))