def findall(at, t):
    res = []
    for i in range(len(at)):
        if at[i]<=t:
            res.append(i)
    return res

def find(p, indices):
    ans = indices[0]
    m = p[ans]
    for i in indices[1:]:
        if m>p[i]:
            m = p[i]
            ans = i
    return ans

n = int(input("enter the number of processes: "))

print("Enter arrival times of processes")
arrival=[int(i) for i in input().split()]
print("Enter burst times of processes")
burst=[int(i) for i in input().split()]
print("Enter priority of each process")
priority=[int(i) for i in input().split()]
#priority start
indx = list(range(n))
tat = [None]*n
waiting = [0]*n
end = tat[:]
t = min(arrival)
cs = 0
reali=None
while arrival:
    indices = findall(arrival, t)
    ind = find(priority, indices)
    temp = indx[ind]
    if temp != reali and reali != None:
        cs+=1
    reali = temp
    for i in indices:
        waiting[indx[i]] += 1
    waiting[reali] -= 1
    burst[ind] -= 1
    t += 1
    if burst[ind]==0:
        tat[reali] = t-arrival[ind]
        end[reali] = t
        arrival.pop(ind)
        burst.pop(ind)
        priority.pop(ind)
        indx.pop(ind)
        

print('Turn Around Time of processes are',tat)
print('Waiting time of processes are',waiting)
print('End time of processes',end)
print()
print('Average Waiting time is', sum(waiting)/n)
print('Average Turn Around time is', sum(tat)/n)
print('Number of Context switches is',cs)

