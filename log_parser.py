import re


log = "192.168.1.1 , Hello"
parts = log.split(" , ")

ip = re.findall(r"\d{1,3}+\.\d{1,3}+\.\d{1,3}+\.\d{1,3}+\b", log)
print("Found IP:" , ip)
