import socket
import datetime

try:
    ip = socket.gethostbyname(socket.gethostname())
    print(f"{datetime.datetime.now()} - VM IP Address: {ip}")
except:
    print("Could not retrieve IP.")