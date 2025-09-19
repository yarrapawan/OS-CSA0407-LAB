filename = input("Enter file name: ")
data = input("Enter data to write into file: ")

f = open(filename, "w")
f.write(data)
f.close()

f = open(filename, "r")
print("File content:", f.read())
f.close()

import os
os.remove(filename)
print("File deleted successfully")
