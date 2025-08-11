
users = {"Alice" : {"ip" : "192.168.1.1", "login": "2025-06-20"}, 
        "Sam" :{"ip" : "10.100.1.1", "login": "2025-07-25"}}

for users, data in users.items():

        print(f"(users): {data["ip"]}")
