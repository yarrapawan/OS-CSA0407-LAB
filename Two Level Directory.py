# Two Level Directory
class TwoLevelDirectory:
    def __init__(self):
        self.directories = {}   # {username: [files]}

    def create_user(self, username):
        if username in self.directories:
            print(f"User '{username}' already exists!")
        else:
            self.directories[username] = []
            print(f"User '{username}' directory created.")

    def create_file(self, username, filename):
        if username not in self.directories:
            print(f"User '{username}' does not exist!")
            return
        if filename in self.directories[username]:
            print(f"File '{filename}' already exists for user '{username}'!")
        else:
            self.directories[username].append(filename)
            print(f"File '{filename}' created for user '{username}'.")

    def display(self):
        print("\nTwo-Level Directory Structure:")
        for user, files in self.directories.items():
            print(f"User: {user}")
            if files:
                for f in files:
                    print(f"  - {f}")
            else:
                print("  (No files)")



tdir = TwoLevelDirectory()
tdir.create_user("Alice")
tdir.create_user("Bob")

tdir.create_file("Alice", "file1.txt")
tdir.create_file("Alice", "notes.doc")
tdir.create_file("Bob", "file1.txt")  
tdir.create_file("Charlie", "demo.txt")  

tdir.display()