import subprocess

def detect_installed_programs():
    """
    This function detects which programs are installed on a Windows system using the 'wmic' command.
    """
    command = 'wmic product get name'
    output = subprocess.check_output(command, shell=True)
    installed_programs = []
    for line in output.splitlines():
        line = line.decode().strip()
        if line:
            installed_programs.append(line)
    return installed_programs


x = detect_installed_programs()
print(x)


