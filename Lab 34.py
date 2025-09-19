n = int(input("Enter number of blocks on disk: "))
disk = [-1] * n
start = int(input("Enter starting block: "))
length = int(input("Enter length of file: "))

if start + length > n:
    print("Not enough space for file")
else:
    for i in range(start, start+length):
        disk[i] = 1
    print("File allocated from block", start, "to", start+length-1)
    print("Disk:", disk)

record = int(input("Enter record number to access: "))
if record < length:
    print("Accessing record", record, "requires reading blocks from", start, "to", start+record)
else:
    print("Invalid record number")
