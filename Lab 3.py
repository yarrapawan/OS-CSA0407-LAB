# first come first serve

n = int(input("Enter the number of processors: "))
burst_time=[]
for i in range(n):
    bt = int(input(f"Enter the Burst time for processors P{(i+1)}: "))
    burst_time.append(bt)
print(f"Burst time: (burst_time)")
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
