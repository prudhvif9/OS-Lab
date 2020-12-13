print("Enter pages that need to access")
pages=[int(i) for i in input().split()]
frames=int(input("Enter number of frames"))
ans=[]
pagefaults=0
def findIndex(x,i):
    pg=[]
    if len(x)<frames:
        return len(x)
    else:
        for j in range(i,len(pages)):
            if pages[j] in x:
                pg.append(pages[j])
            if len(pg)==frames-1:
                break
        values=[]
        for j in x:
            if j not in pg:
                values.append(j)
        min=1000
        for k in values:
            if x.index(k)<min:
                min=x.index(k)
        return min
                
        
l=[None]*frames
ans=[]
for i in range(len(pages)):
    if pages[i] not in l:
        pagefaults+=1
        x=[]
        for j in l:
            if j==None:
                break
            x.append(j)
        ind=findIndex(x,i)
        l[ind]=pages[i]   
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
        
