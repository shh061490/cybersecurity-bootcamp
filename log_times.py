import os
import datetime

# Step 1: Pick the folder (the toy box)
folder = r"C:\Windows\Logs"

try:
    # Step 2: Look inside the folder
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        # Step 3: Only check if it's really a file
        if os.path.isfile(path):
            # Step 4: Find last time it was changed
            mtime = os.path.getmtime(path)
            last_time = datetime.datetime.fromtimestamp(mtime)

            # Step 5: Print name + time in nice format
            print(f"{file} - {last_time.strftime('%Y-%m-%d %H:%M:%S')}")

except Exception as e:
    # Step 6: Catch any "uh-oh"
    print("Oops! Something went wrong:", e)

