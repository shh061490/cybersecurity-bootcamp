import subprocess
from datetime import datetime
def test_ping(ip_address):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = subprocess.run(["ping", "-n", "4", ip_address], capture_output=True, text=True)
        status = "succeeded" if result.returncode == 0 else "failed"
        print(f"Ping to {ip_address} {status} at {timestamp} (Layer 3: Network)")
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    test_ping(input("What IP do you want to ping: "))