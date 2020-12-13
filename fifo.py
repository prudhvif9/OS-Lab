print("Enter pages that need to access")
pages=[int(i) for i in input().split()]
frames=int(input("Enter number of frames "))
ans=[]
l=[None]*frames
id=0
pagefaults=0
for i in pages:
    if i not in l:
        pagefaults+=1
        l[id]=i
        id+=1
        if id==frames:
            id=0
    x=[]
    for j in l:
        x.append(j)
    ans.append(x)
for i in range(frames):
    for j in range(len(ans)):
        if ans[j][i]==None:
            print(" ",end=" ")
        else:
            print(ans[j][i],end=" ")
    print()
print("Number of Page Faults are ",pagefaults)
