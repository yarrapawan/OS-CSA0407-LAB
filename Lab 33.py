# Optimal Page Replacement

pages = list(map(int, input("Enter the reference string (space separated): ").split()))
capacity = int(input("Enter the number of frames: "))

frames = []
page_faults = 0

for i in range(len(pages)):
    p = pages[i]
    if p not in frames:
        if len(frames) < capacity:
            frames.append(p)
        else:
            farthest = -1
            replace_index = -1
            for j in range(len(frames)):
                if frames[j] in pages[i+1:]:
                    next_use = pages[i+1:].index(frames[j]) + i + 1
                else:
                    next_use = 999999
                if next_use > farthest:
                    farthest = next_use
                    replace_index = j
            frames[replace_index] = p
        page_faults += 1
    print(f"Page {p} -> {frames}")

print("Total Page Faults (Optimal):", page_faults)
