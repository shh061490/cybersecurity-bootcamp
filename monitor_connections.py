import psutil
import time
from datetime import datetime


def list_tcp_connections():
    connections = psutil.net_connections(kind='tcp')
    for conn in connections:
        if conn.status == 'ESTABLISHED':
            print(f"Local Address: {conn.laddr.ip}:{conn.laddr.port}, "
                  f"Remote Address: {conn.raddr.ip}:{conn.raddr.port}, "
                  f"Status: {conn.status}")
            
def main():
    """Runs the connection check 3 times with a 10-second interval."""
    iterations = 3
    interval = 10

    for i in range(iterations):
        list_tcp_connections()
        if i < iterations - 1:
            print(f"\nWaiting {interval} seconds...\n")
            time.sleep(interval)

if __name__ == "__main__":
    main()

# Example usage
list_tcp_connections()
