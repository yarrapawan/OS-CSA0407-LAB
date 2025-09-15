# Bankers Algorithm (deadlock)

import numpy as np

# Input number of processes and resource types
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

# Input Available resources
available = []
for i in range(m):
    val = int(input(f"Enter available units of Resource {i}: "))
    available.append(val)
available = np.array(available)

# Input Allocation matrix
allocation = []
print("Enter allocation matrix (each row for a process):")
for i in range(n):
    row = list(map(int, input(f"P{i} allocation: ").split()))
    allocation.append(row)
allocation = np.array(allocation)

# Input Maximum Requirement matrix
max_req = []
print("Enter maximum requirement matrix (each row for a process):")
for i in range(n):
    row = list(map(int, input(f"P{i} max need: ").split()))
    max_req.append(row)
max_req = np.array(max_req)

# Calculate Need matrix
need = max_req - allocation

# Initialize
finish = [False]*n
safe_seq = []

# Banker’s Algorithm
while len(safe_seq) < n:
    allocated = False
    for i in range(n):
        if not finish[i] and all(need[i] <= available):
            available += allocation[i]
            finish[i] = True
            safe_seq.append(i)
            allocated = True
    if not allocated:
        break

# Display result
if len(safe_seq) == n:
    print("System is in SAFE state.")
    print("Safe sequence:", ["P"+str(i) for i in safe_seq])
else:
    print("System is in UNSAFE state! Deadlock may occur.")
