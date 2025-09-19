import os

filename = input("Enter file name: ")
data = input("Enter data: ")

f = open(filename, "w+")
f.write(data)
f.seek(0)
print("After seek ->", f.read())
f.close()

info = os.stat(filename)
print("File Size:", info.st_size)

dirname = input("Enter directory to list: ")
print("Files in directory:", os.listdir(dirname))
