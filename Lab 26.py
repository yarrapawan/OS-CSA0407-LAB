filename = input("Enter file name: ")
data = input("Enter text to write: ")

f = open(filename, "w")
f.write(data)
f.close()

f = open(filename, "r")
print("File read:", f.read())
f.close()

f = open(filename, "a")
more = input("Enter text to append: ")
f.write(more)
f.close()

f = open(filename, "r")
print("After append:", f.read())
f.close()

import os
os.remove(filename)
print("File deleted")
