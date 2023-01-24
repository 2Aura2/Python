import os
import subprocess

def scan_file(file_path):
    result = subprocess.run(['clamscan', '--stdout', '-r', file_path], capture_output=True)
    return result.stdout.decode()

def main():
    file_path = input("Enter the file path: ")
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return

    scan_result = scan_file(file_path)
    if "Infected files: 0" in scan_result:
        print("The file is clean.")
    else:
        print("The file is infected.")

if __name__ == '__main__':
    main()