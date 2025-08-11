
users = {"Sam": 25, "Bob" : 30}

print(users["Sam"])

# Safely get value for "chalie"
print(users.get("charlie", "Not Found"))

# Add a new user
users["charlie"] = 28

print(users)

