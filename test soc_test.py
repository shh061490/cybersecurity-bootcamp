import socket
localhost = "127.0.0.1"
for port in [80, 443]:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout to 1 second
            result = s.connect_ex((localhost, port))
            print(f"Port {port} is", "open" if result == 0 else "closed")
    except socket.error as e:
        print(f"Error scanning port {port}: {e}")







