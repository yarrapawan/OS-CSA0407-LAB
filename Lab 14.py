# Single-level directory
directory = {}

# Create files
filename = "file1.txt"
content = "Hello World"
if filename in directory:
    print("File already exists")
else:
    directory[filename] = content
    print(f"File '{filename}' created.")

filename = "file2.txt"
content = "Python OS Lab"
if filename in directory:
    print("File already exists")
else:
    directory[filename] = content
    print(f"File '{filename}' created.")

# Display files
print("Files in directory:", list(directory.keys()))

# Delete a file
filename = "file1.txt"
if filename in directory:
    del directory[filename]
    print(f"File '{filename}' deleted.")
else:
    print("File not found.")

# Display after deletion
print("Files in directory:", list(directory.keys()))
