# Various Memory Aloocation

def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
    return allocation


def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        best_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_index == -1 or blocks[j] < blocks[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            blocks[best_index] -= processes[i]
    return allocation


def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        worst_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_index == -1 or blocks[j] > blocks[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            blocks[worst_index] -= processes[i]
    return allocation


def display(processes, allocation, strategy_name):
    print(f"\n{strategy_name} Allocation:")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"{i+1}\t\t{processes[i]}\t\t{allocation[i]+1}")
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")



processes = [212, 417, 112, 426]
blocks = [100, 500, 200, 300, 600]

print("Processes:", processes)
print("Memory Blocks:", blocks)

alloc1 = first_fit(blocks.copy(), processes)
display(processes, alloc1, "First Fit")

alloc2 = best_fit(blocks.copy(), processes)
display(processes, alloc2, "Best Fit")


alloc3 = worst_fit(blocks.copy(), processes)
display(processes, alloc3, "Worst Fit")