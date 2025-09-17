# First Fit Memory Allocation in Python

# Input number of blocks and processes
n_blocks = int(input("Enter number of memory blocks: "))
block_size = []
for i in range(n_blocks):
    block_size.append(int(input(f"Enter size of block {i+1}: ")))

n_processes = int(input("\nEnter number of processes: "))
process_size = []
for i in range(n_processes):
    process_size.append(int(input(f"Enter size of process {i+1}: ")))

# Allocation array to store block assigned to process (-1 means not allocated)
allocation = [-1] * n_processes

# First Fit Allocation
for i in range(n_processes):
    for j in range(n_blocks):
        if block_size[j] >= process_size[i]:   # if block can hold the process
            allocation[i] = j
            block_size[j] -= process_size[i]   # reduce available block size
            break

# Output
print("\nProcess No.\tProcess Size\tBlock No.")
for i in range(n_processes):
    print(f"{i+1}\t\t\t{process_size[i]}\t\t\t\t", end="")
    if allocation[i] != -1:
        print(allocation[i] + 1)
    else:
        print("Not Allocated")
