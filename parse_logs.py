import csv
import os

# Step 1: Find the Docuemnts Folder
file_path = os.path.expanduser("~/Documents/security_log.csv")

# Step 2 Open the log file
with open(file_path, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    print(f"Failed login attempts (Event ID 4625):\n")

    # Step 3: Go through each row and look for Event ID 4625
    for row in reader:
        if row.get("EventID") == "4625":
            time = row.get("TimeCreated") or row.get("Date")
            user = row.get("Account Name") or row.get("User")
            print(f"Time: {time} | User: {user}")





# Directly point to Documents folder
