# LRU Page Replacement

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
            lru_index = -1
            lru_age = 999999
            for j in range(len(frames)):
                if frames[j] in pages[:i]:
                    last_used = max(k for k in range(i) if pages[k] == frames[j])
                else:
                    last_used = -1
                if last_used < lru_age:
                    lru_age = last_used
                    lru_index = j
            frames[lru_index] = p
        page_faults += 1
    print(f"Page {p} -> {frames}")

print("Total Page Faults (LRU):", page_faults)
