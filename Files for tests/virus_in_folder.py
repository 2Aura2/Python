import os
import hashlib

#get hash of file
def md5_hash(filename):
    with open(filename,"rb")as f:
        bytes = f.read()
        md5hash = hashlib.md5(bytes).hexdigest()
        f.close()
    return md5hash

#print(md5_hash("Images\\Background.jpg"))

def check_folder_virus(folder_path):
    # Loop through all files in the specified folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)
            # Open the file and read its contents
            with open(file_path, 'rb') as f:
                file_data = f.read()
                #print(file_data)
                #print()
            # Create a hash of the file contents
            m = hashlib.md5()
            m.update(file_data)
            file_hash = m.hexdigest()
            # Check the file hash against a database of known virus hashes
            # This is where you would need to implement a database or external service
            # to check the file hash against a list of known virus hashes
            known_virus_hashes = ["d5520a7f8caa7dd98e821f387cbf4f06","d72dc0459c292fe5b6d787cc5dd38447","0624e866088087793e074e98c5d90baa"]
            if file_hash in known_virus_hashes:
                print(f"Virus detected in file: {file_path}")
    print("Scan complete. No more virus detected.")

check_folder_virus("C:\\Users\\dato0\\OneDrive\\שולחן העבודה\\New folder (2)")