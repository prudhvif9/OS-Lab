print("Enter pages that need to access")
pages=[int(i) for i in input().split()]
frames=int(input("Enter number of frames"))
priority=[i for i in range(1,frames+1)]
ans=[]
pagefaults=0
l=[None]*frames
for i in pages:
    if i not in l:
        pagefaults+=1
        ind=priority.index(1)
        l[ind]=i
        for j in range(frames):
            if j!=ind:
                priority[j]-=1
        priority[ind]=frames
    else:
        ind=l.index(i)
        for j in range(frames):
            if priority[j]!=1:
                priority[j]-=1
        priority[ind]=frames
    x=[]
    for i in l:
        x.append(i)
    ans.append(x)
for i in range(frames):
    for j in range(len(ans)):
        if ans[j][i]==None:
            print(" ",end=" ")
        else:
            print(ans[j][i],end=" ")
    print()
print("Number of Page Faults are ",pagefaults)
