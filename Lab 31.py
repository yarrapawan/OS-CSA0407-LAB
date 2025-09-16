# FIFO Page Replacement

pages = list(map(int, input("Enter the reference string (space separated): ").split()))
capacity = int(input("Enter the number of frames: "))

frames = []
page_faults = 0

for p in pages:
    if p not in frames:
        if len(frames) < capacity:
            frames.append(p)
        else:
            frames.pop(0)
            frames.append(p)
        page_faults += 1
    print(f"Page {p} -> {frames}")

print("Total Page Faults (FIFO):", page_faults)
