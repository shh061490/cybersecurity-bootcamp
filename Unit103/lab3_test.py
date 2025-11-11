import os


folder = "C:\\"
extension = ".txt"


for root, _, files in os.walk(folder):
   for file in files:
       if file.endswith(extension):
           print(os.path.join(root, file))