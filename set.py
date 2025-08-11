
logs = ["192.168.1.1", "10.0.0.1", "192.168.1.1"]
unique_logs = set(logs)
print(unique_logs)


logs2 = ["10.0.0.1", "172.16.0.1"]
print(unique_logs & set(logs2))