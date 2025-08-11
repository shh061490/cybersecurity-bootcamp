import socket

localhost = "127.0.0.1"

for port in [80, 443]:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        result = s.connect_ex((localhost, port))
        print(f"Port {port} is", "open" if result == 0 else "closed")
