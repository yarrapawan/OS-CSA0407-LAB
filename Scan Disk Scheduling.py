# SCAN Disk Scheduling in Python

# Input
size = int(input("Enter number of requests: "))
requests = list(map(int, input("Enter request sequence: ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter total disk size (cylinders): "))
direction = input("Enter initial direction (left/right): ").lower()

# Add head position
seek_sequence = []
seek_time = 0
current = head

# Split requests into left and right of head
left = [0]   # include 0 (start of disk)
right = [disk_size - 1]  # include end of disk

for r in requests:
    if r < head:
        left.append(r)
    if r > head:
        right.append(r)

left.sort()
right.sort()

# SCAN algorithm
if direction == "left":
    # Move left first, then right
    for r in reversed(left):
        seek_sequence.append(r)
        seek_time += abs(current - r)
        current = r
    for r in right:
        seek_sequence.append(r)
        seek_time += abs(current - r)
        current = r
else:
    # Move right first, then left
    for r in right:
        seek_sequence.append(r)
        seek_time += abs(current - r)
        current = r
    for r in reversed(left):
        seek_sequence.append(r)
        seek_time += abs(current - r)
        current = r

# Output
print("\nSeek Sequence:", seek_sequence)
print("Total Seek Time:", seek_time)
