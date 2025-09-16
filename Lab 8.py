n = int(input("Enter the number of processes: "))
burst_time = []
for i in range(n):
    bt = int(input(f"Enter Burst time for process P{i+1}: "))
    burst_time.append(bt)

time_quantum = int(input("Enter Time Quantum: "))

remaining_time = burst_time[:]
waiting_time = [0]*n
turnaround_time = [0]*n
completion_time = [0]*n

time = 0
done = 0

while done < n:
    idle = True
    for i in range(n):
        if remaining_time[i] > 0:
            idle = False
            if remaining_time[i] > time_quantum:
                time += time_quantum
                remaining_time[i] -= time_quantum
            else:
                time += remaining_time[i]
                remaining_time[i] = 0
                completion_time[i] = time
                turnaround_time[i] = completion_time[i]
                waiting_time[i] = turnaround_time[i] - burst_time[i]
                done += 1
    if idle:
        time += 1
        
print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{i+1}\t\t{burst_time[i]}\t\t\t{waiting_time[i]}\t\t\t{turnaround_time[i]}")

avg_wt = sum(waiting_time)/n
avg_tat = sum(turnaround_time)/n
print(f"Average Waiting Time: {avg_wt}")
print(f"Average Turnaround Time: {avg_tat}")

        
n = int(input("Enter the no of resources: "))
burst_time = []
for i in range(n):
    bt = input(f"Enter the burst time for the process P{i+1}: ")
    burst_time.append(bt)
quantum_time = int(input("Enter the quantum time: "))
waiting_ime = [0]*n
turnaround_time = [0]*n
completion_time = [0]*n
time = 0
done = 0

while done < n:
    idle = True
    for i in range(n):
        if remaining_time[i] > 0:
            idle = False
            if remaining_time[i] > quantum_time:
                time += quantum_time[i]
                remaining_time[i] -= quantum_time
            else:
                time += remainig_time[i]
                remaining_time[i] = 0
                completion_time[i] = time
                turnaround_time[i] = completion_time[i]
                waiting_time[i] = turnaround_time[i] - burst_time[i]
                done += 1
    if idle:
        time += 1
                
print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{i+1}\t\t{burst_time[i]}\t\t\t{waiting_time[i]}\t\t\t{turnaround_time[i]}")

avg_wt = sum(waiting_time)/n
avg_tat = sum(turnaround_time)/n
print(f"Average Waiting Time: {avg_wt}")
print(f"Average Turnaround Time: {avg_tat}")
