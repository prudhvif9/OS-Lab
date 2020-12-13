n = int(input("enter the number of processes: "))
print("Enter arrival times of processes")
arrival=[int(i) for i in input().split()]
print("Enter burst times of processes")
burst=[int(i) for i in input().split()]

tat = []
waiting = []
end = []
contextswitch = n-1

waiting.append(0)
tat.append(burst[0])
t = burst[0]+arrival[0]
end.append(t)
for i in range(1,n):
    if t>arrival[i]:
        waiting.append(t-arrival[i])
    else:
        waiting.append(0)
        t = arrival[i]
    t += burst[i]
    tat.append(t-arrival[i])
    end.append(t)

print('Turn Around Time of processes are',tat)
print('Waiting time of processes are',waiting)
print('End time of processes',end)
print()
print('Average Waiting time is', sum(waiting)/n)
print('Average Turn Around time is', sum(tat)/n)
print('Number of Context switches is',contextswitch)
