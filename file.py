
import requests

# Write to file
with open("test.txt", "w") as f:
    f.write("Sample log\n")

# Read file
with open("test.txt", "r") as f:
    print(f.read())
