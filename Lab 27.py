import os

dirname = input("Enter directory name: ")
files = os.listdir(dirname)
for f in files:
    print(f)
