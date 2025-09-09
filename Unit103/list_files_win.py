
import os

username = "SHH"
path = f"C:\\Users\\{username}"

folder_path = os.path.expanduser("~")
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

print("Files only:")
for file in files:
    print(file)
        