#Write a program that takes a list of IPs (e.g.,  ["192.168.1.1, "10.0.0.1, "192.168.1.1"])
#Returns unique, sorted IPs.
#Eample output: ["10.0.0.1", "192.168.1.1"]

def ips_list(ip):
    return sorted(list(set(ip)))
ip = ["100.20.1.1", "10.50.100.3", "172.192.1.1"]
print(ips_list(ip))