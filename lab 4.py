# Shortest Job First Scheduling

n = int(input("Enter the number of Processes: "))
burst_time=[]

for i in range(n):
    bt = int(input(f"Enter the Burst time for the processor({i+1}): "))
    burst_time.append(bt)

processes = [f"p{i+1}"for i in range(n)]

for i in range(n):
    for j in range(i+1,n):
        if burst_time[i]>burst_time[j]:
            burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
            processes[i], processes[j] = processes[j], processes[i]
            
waiting_time = [0]*n
turnaround_time = [0]*n

for i in range(1,n):
    waiting_time[i] = waiting_time[i-1]+burst_time[i-1]

for i in range(n):
    turnaround_time[i] = waiting_time[i]+burst_time[i]

print("Process\tBurst time\tWaiting time\tTurn around time")
for i in range(n):
    print(f"P{i+1}\t\t{burst_time[i]}\t\t\t{waiting_time[i]}\t\t\t\t{turnaround_time[i]}")

avg_w_t = sum(waiting_time)/n
avg_t_t = sum(turnaround_time)/n
print(f"Avergae Waiting time is: {avg_w_t}, \n Average Turnaround Time is: {avg_t_t}") 

            