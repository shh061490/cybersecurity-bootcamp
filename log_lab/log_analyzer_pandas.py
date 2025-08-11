import pandas as pd
df = pd.read_csv("logs.csv")
result = df.groupby("ip")["count"].sum()
for ip, count in result.items():
    print(f"IP {ip}: {count}")
