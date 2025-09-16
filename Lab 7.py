# Non-Preemptive Shortest Job First (SJF) Scheduling

n = int(input("Enter the Number of Processes: "))
arrival_time = []
burst_time = []
processes = [f"P{i+1}" for i in range(n)]

for i in range(n):
    at = int(input(f"Enter the Arrival Time for process {processes[i]}: "))
    bt = int(input(f"Enter the Burst Time for process {processes[i]}: "))
    arrival_time.append(at)
    burst_time.append(bt)

waiting_time = [0] * n
turnaround_time = [0] * n
completion_time = [0] * n
is_completed = [False] * n

time = 0
completed = 0


while completed < n:
    idx = -1
    min_bt = 9999999
    for i in range(n):
        if arrival_time[i] <= time and not is_completed[i]:
            if burst_time[i] < min_bt:
                min_bt = burst_time[i]
                idx = i
            elif burst_time[i] == min_bt:
                if arrival_time[i] < arrival_time[idx]:
                    idx = i

    if idx != -1:
        time += burst_time[idx]
        completion_time[idx] = time
        turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
        is_completed[idx] = True
        completed += 1
    else:
        time += 1

print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{processes[i]}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n
print(f"\nAverage Waiting Time: {avg_wt}")
print(f"Average Turnaround Time: {avg_tat}")
