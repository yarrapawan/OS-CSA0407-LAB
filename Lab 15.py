# Two-level directory
root = {}

# Create directories
dirname = "docs"
if dirname in root:
    print("Directory already exists")
else:
    root[dirname] = {}
    print(f"Directory '{dirname}' created.")

dirname = "images"
if dirname in root:
    print("Directory already exists")
else:
    root[dirname] = {}
    print(f"Directory '{dirname}' created.")

# Create files in directories
dirname = "docs"
filename = "file1.txt"
content = "Document content"
if filename in root[dirname]:
    print("File already exists")
else:
    root[dirname][filename] = content
    print(f"File '{filename}' created in directory '{dirname}'")

dirname = "images"
filename = "image1.png"
content = "Image content"
if filename in root[dirname]:
    print("File already exists")
else:
    root[dirname][filename] = content
    print(f"File '{filename}' created in directory '{dirname}'")

# Display structure
for d in root:
    print(f"Directory: {d}, Files: {list(root[d].keys())}")
