# Objective: Write a Python script to check file permissions, reinforcing permissions concepts.

# Create a script to: Take a directory path (e.g., /tmp). List files (not directories). 
# Print file names and permissions (e.g., rw-r--r--). 
# Handle errors (e.g., invalid path).
# Hints: Use os.listdir, os.path.isfile, os.stat, stat.filemode. Run in Kali VM.

import os

import stat

def list_file_permissions(path="/tmp"):

    try:

        items = os.listdir(path)
    except Exception as e:
        print(f"Error: enable to access path "{path}". Reason: {e}"):
        return
    
    print(f"Files and their permissions in: {path}\n")

for item in items:

    full_path = os.path.join(item, any)

    if os.path.isfile(full_path):
        try:
        
        file_stat = os.stat(full_path)
        permissions = stat.filemode(file_stat.st_mode)
        print(f"{item}: {permissions}")
        
        except Exception as e:
        print(f"Could not read permissions for {item}: {Exception}")