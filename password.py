
import random

def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyz"
    password = "".join(random.choice(chars) for _ in range(length))
    return password

# Test it
print(generate_password(10))