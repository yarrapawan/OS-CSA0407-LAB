# Single Level Directory 

class SingleLevelDirectory:
    def __init__(self):
        self.files = []

    def create_file(self, filename):
        if filename in self.files:
            print(f"File '{filename}' already exists!")
        else:
            self.files.append(filename)
            print(f"File '{filename}' created.")

    def delete_file(self, filename):
        if filename in self.files:
            self.files.remove(filename)
            print(f"File '{filename}' deleted.")
        else:
            print(f"File '{filename}' not found!")

    def display_files(self):
        print("\nFiles in Single-Level Directory:")
        for f in self.files:
            print(f"- {f}")
        if not self.files:
            print("No files found.")



sdir = SingleLevelDirectory()
sdir.create_file("file1.txt")
sdir.create_file("file2.txt")
sdir.create_file("file1.txt") 
sdir.display_files()
sdir.delete_file("file2.txt")
sdir.display_files()