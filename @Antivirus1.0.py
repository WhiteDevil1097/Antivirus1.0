import os
import hashlib
logo = '''⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⣰⡾⠛⠛⠉⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⢀⣿⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠸⣧⡀⠀⠀⠀⠀⠀⠀⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠈⠻⣦⣀⣀⣀⣠⣾⠷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣤⡤⠀
⠀⠀⠀⠀⠀⠀           ⠈⠛⠉⠉⠙⣷⣴⠟⠛⣷⣄⠀⠀⠀⠀⢿⡟⠛⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀           ⠀⠀⠀⠈⠻⣦⡾⠋⢙⣷⣄⠀⠀⢸⡇⠀⢠⡶⣶⣦⣤⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀           ⠀⠀⠀⠀⠈⠻⣶⡟⠉⣹⣷⣄⠘⣿⢀⣿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           ⠀⠀⠀⠀⠈⠻⣿⡏⢀⣿⢷⣿⣾⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣁⣴⠟⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀             ⠀⠀⠀⠀⠀⠻⣿⡿⠷⢶⣾⣿⣷⣴⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀          ⠀⠀⣀⣨⣿⣾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀           ⠀⠀⠀⠀⢸⣿⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       ⠀⠀⠀⠛⠀⠀⠀⠈⠛⠂⠀⠀⠀⠀'''
print(logo)
print("              Antivirus1.0  ")
# Define a function to scan files for viruses
def scan_file(file_path):
    # Calculate the MD5 hash of the file
    md5_hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
    
    # Check the hash against a database of known viruses (this is a very basic implementation)
    virus_db = {
        'known_virus_1': '0123456789abcdef',
        'known_virus_2': 'fedcba9876543210'
    }
    
    if md5_hash in virus_db.values():
        return f"Virus detected: {file_path}"
    else:
        return f"File is clean: {file_path}"

# Define a function to scan a directory for viruses
def scan_dir(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            result = scan_file(file_path)
            print(result)

# Define the main function
def termux_antivirus():
    print("Termux Antivirus v1.0")
    print("Scanning for viruses...")
    
    # Set the directory to scan (e.g. /sdcard or /storage/emulated/0)
    directory = '/sdcard'
    
    scan_dir(directory)

# Run the main function
termux_antivirus()
