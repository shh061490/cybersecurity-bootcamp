
# socket.py

import socket

# Optional: set timeout to avoid hanging
s = socket.socket()
s.settimeout(1)  # seconds

# Try connecting to localhost on port 80
result = s.connect_ex(("localhost", 80))

# Print result
print("Port open" if result == 0 else "Port closed")

s.close()