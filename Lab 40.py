users = ["owner", "group", "others"]
permissions = {"r": "Read", "w": "Write", "x": "Execute"}

perm = input("Enter permission string (like rwx, r--): ")
for i in range(3):
    print(users[i], "permissions:")
    for j in range(3):
        if perm[i*3 + j] != "-":
            print(" ", permissions[perm[i*3 + j]])

