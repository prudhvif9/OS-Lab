def findall(at, t):
    res = []
    for i in range(len(at)):
        if at[i]<=t:
            res.append(i)
    return res

def find(bt, indices):
    ans = indices[0]
    m = bt[ans]
    for i in indices[1:]:
        if m>bt[i]:
            m = bt[i]
            ans = i
    return ans

n = int(input("enter the number of processes: "))
print("Enter arrival times of processes")
arrival=[int(i) for i in input().split()]
print("Enter burst times of processes")
burst=[int(i) for i in input().split()]

#sjf non preemtive start
indx = [i for i in range(n)]
tat = [None]*n
waiting = tat[:]
end = tat[:]
cs = n-1
t = min(arrival)
while arrival:
    indices = findall(arrival, t)
    ind = find(burst, indices)
    currat = arrival.pop(ind)
    currbt = burst.pop(ind)
    reali = indx.pop(ind)
    if t>currat:
        waiting[reali] = t-currat
    else:
        waiting[reali] = 0
        t = currat
    t += currbt
    tat[reali] = t-currat
    end[reali] = t
#sjf ends

print()
print('Turn Around Time of processes are',tat)
print('Waiting time of processes are',waiting)
print('End time of processes',end)
print()
print('Average Waiting time is', sum(waiting)/n)
print('Average Turn Around time is', sum(tat)/n)
print('Number of Context switches is',cs)

# 5
# 7
# 2
# 5
# 4
# 6
# 0
# 2
# 3
# 5
# 7
