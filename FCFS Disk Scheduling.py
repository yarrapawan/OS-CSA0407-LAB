# FCFS Disk Scheduling in Python

# Input
n = int(input("Enter number of requests: "))
requests = list(map(int, input("Enter request sequence: ").split()))
head = int(input("Enter initial head position: "))

# Processing
seek_sequence = []
seek_time = 0
current = head

for req in requests:
    seek_sequence.append(req)
    seek_time += abs(current - req)
    current = req

# Output
print("\nSeek Sequence:", seek_sequence)
print("Total Seek Time:", seek_time)
print("Average Seek Time:", seek_time / n)
