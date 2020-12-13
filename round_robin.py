def find(at, t):
    res = None
    ind = None
    for i in range(len(at)):
        if at[i]<=t and (res==None or res>at[i]):
            res = at[i]
            ind = i
    return ind

n = int(input("enter the number of processes: "))
print("Enter arrival times of processes")
arrival=[int(i) for i in input().split()]
print("Enter burst times of processes")
burst=[int(i) for i in input().split()]
qt = int(input('enter quantum time: '))

# fcfs starts

at_old = arrival[:]
indx = list(range(n))
tat = [0]*n
waiting = [0]*n
end = [0]*n
cs = 0
t = min(arrival)
reali = None

while arrival:
    ind = find(arrival, t)
    if ind==None:
        t+=1
        continue
    temp = indx[ind]
    if temp != reali and reali != None:
        cs+=1
    reali = temp
    if t>arrival[ind]:
        waiting[reali] += t-arrival[ind]
    else:
        t = arrival[ind]
    arrival.pop(ind)
    if burst[ind]>qt:
        t += qt
        arrival.append(t)
        burst.append(burst.pop(ind) - qt)
        indx.append(indx.pop(ind))
    else:
        t += burst[ind]
        tat[reali] = t-at_old[reali]
        end[reali] = t
        burst.pop(ind)
        indx.pop(ind)
    
# fcfs ends
print()
print('Turn Around Time of processes are',tat)
print('Waiting time of processes are',waiting)
print('End time of processes',end)
print()
print('Average Waiting time is', sum(waiting)/n)
print('Average Turn Around time is', sum(tat)/n)
print('Number of Context switches is',cs)
