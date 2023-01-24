import hashlib

def check_virus(file_path):
    # Open the file and read its contents
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Create a hash of the file contents
    m = hashlib.md5()
    m.update(file_data)
    print(m)
    file_hash = m.hexdigest()
    known_virus_hashes = ["d5520a7f8caa7dd98e821f387cbf4f06","d72dc0459c292fe5b6d787cc5dd38447"]
    # Check the file hash against a database of known virus hashes
    # This is where you would need to implement a database or external service
    # to check the file hash against a list of known virus hashes
    if file_hash in known_virus_hashes:
        return "Virus detected!"
    else:
        return "No virus detected."

print(check_virus("D:\\School Project\\Python\\Images\\784p9o.webp"))