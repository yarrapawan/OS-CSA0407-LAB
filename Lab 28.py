filename = input("Enter file name: ")
pattern = input("Enter word to search: ")

f = open(filename, "r")
for line in f:
    if pattern in line:
        print(line.strip())
f.close()
