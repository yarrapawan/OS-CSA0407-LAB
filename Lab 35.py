n = int(input("Enter number of blocks: "))
disk = [-1] * n
index_block = int(input("Enter index block: "))
length = int(input("Enter number of blocks for file: "))
blocks = []

for i in range(length):
    b = int(input("Enter block number for file: "))
    if disk[b] == -1 and b != index_block:
        disk[b] = 1
        blocks.append(b)
    else:
        print("Block already allocated, try again")

print("Index Block:", index_block, "->", blocks)
print("Disk:", disk)
