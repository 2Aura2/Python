import hashlib
import os

#get hash of file
def sha256_hash(filename):
    with open(filename,"rb")as f:
        bytes = f.read()
        sha256hash = hashlib.sha256(bytes).hexdigest()
        f.close()
        print(sha256hash)
    return sha256hash


#print(md5_hash("Images\\Anti_Virus_BG.jpg"))
#print(md5_hash("Images\\Background.jpg"))
#print(md5_hash("Images\\Settings Button.png"))
#print(md5_hash("Images\\thumb-1920-77840.jpg"))


def malware_checker(PathOfFile):
    hash_malware_check = sha256_hash(PathOfFile)
    
    malware_hashes = open("Files for tests\\virushash.txt","r")
    malware_hashes_read = malware_hashes.read()
    malware_hashes.close()
    
    virusinfo = open("Files for tests\\virusinfo.txt","r").readlines()
    
    if malware_hashes_read.find(hash_malware_check) != -1:
        return virusinfo[malware_hashes_read.index(hash_malware_check)]
        #print(virusinfo.index(str(malware_hashes_read.index(hash_malware_check))))
    else:
        return 0



malware_hashes = list(open("Files for tests\\virushash.txt","r").read().split('\n'))

virusinfo = list(open("Files for tests\\virusinfo.txt","r").read().split('\n'))
    

#malware detection by hash    
def malware_checker(PathOfFile):
    global malware_hashes
    global virusinfo
    
    hash_malware_check = sha256_hash(PathOfFile)
    counter = 0

    
    for i in malware_hashes:
        if i == hash_malware_check:
            return virusinfo[counter]
        counter += 1

    return 0
        
    
#print(malware_checker("Images\\784p9o.webp"))



#malware detection in folder
virusname = []
def folderscanner():
    path="C:\\Users\\dato0\\OneDrive\\שולחן העבודה\\New folder (2)"
    dir_list = os.listdir(path)
    fileN=""
    for i in dir_list:
        fileN = path+"\\"+i
        print(fileN)
        if malware_checker(fileN) != 0:
            virusname.append(malware_checker(fileN)+" :: File :: "+i)

folderscanner()
print(virusname)