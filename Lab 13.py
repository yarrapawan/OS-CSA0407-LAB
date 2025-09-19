# Memory blocks and processes
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

# First Fit
ff_blocks = blocks.copy()
ff_alloc = [-1]*len(processes)
for i in range(len(processes)):
    for j in range(len(ff_blocks)):
        if ff_blocks[j] >= processes[i]:
            ff_alloc[i] = j
            ff_blocks[j] -= processes[i]
            break
print("First Fit Allocation:", ff_alloc)

# Best Fit
bf_blocks = blocks.copy()
bf_alloc = [-1]*len(processes)
for i in range(len(processes)):
    best_idx = -1
    for j in range(len(bf_blocks)):
        if bf_blocks[j] >= processes[i]:
            if best_idx == -1 or bf_blocks[j] < bf_blocks[best_idx]:
                best_idx = j
    if best_idx != -1:
        bf_alloc[i] = best_idx
        bf_blocks[best_idx] -= processes[i]
print("Best Fit Allocation:", bf_alloc)

# Worst Fit
wf_blocks = blocks.copy()
wf_alloc = [-1]*len(processes)
for i in range(len(processes)):
    worst_idx = -1
    for j in range(len(wf_blocks)):
        if wf_blocks[j] >= processes[i]:
            if worst_idx == -1 or wf_blocks[j] > wf_blocks[worst_idx]:
                worst_idx = j
    if worst_idx != -1:
        wf_alloc[i] = worst_idx
        wf_blocks[worst_idx] -= processes[i]
print("Worst Fit Allocation:", wf_alloc)
