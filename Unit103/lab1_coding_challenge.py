# Write a Python script to list directories, reinforcing navigation skills
# Task: Script to: Take a directory path F(e.g., /home).
# List only directories (not files).
# Print direcory names.  Handle errors (e.g. invalid path)
# Hints: Use os.listdir, os.path.isdir, os.path.join.  Run in Kali VM. Use try/except.

import os


items = os.listdir, os.path.isdir, os.path.join



# Here we are checking for the current directory

def list_directories_like_ls_d(path="."):
    
    entries = os.listdir(path)
    directories = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
    return directories




        