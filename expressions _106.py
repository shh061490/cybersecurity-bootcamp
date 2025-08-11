
import re

log = "IP: 192.168.1.1, Time: 2025-06-20"
parts = log.split(", ")
print(parts[0 : 3])
ip = re.search(r"\d+\.\d+\.\d+\.\d+", log)
print(ip.groups())
# This is an update to puch the file to GitHub