def find(lis, page, n):
 for i in range(n):
 if lis[i]==page:
 return i
 return None
def findmin(counts, n):
 mini = counts[0]
indx = 0
 for i in range(1, n):
 if counts[i] < mini:
 mini = counts[i]
indx = i
 return indx
pages = list(map(str, input('enter the pages that need to be accessed: ').split()))
frames = int(input('enter number of frames: '))
n = len(pages)
lis = [None]*frames
counts = [0]*frames
ans = []
stack = []
pf = 0
for i in range(n):
 change = True
ind = find(lis, pages[i], frames)
 if ind != None:
 counts[ind] += 1
 change = False
 else:
ind = findmin(counts, frames)
lis[ind] = pages[i]
 counts[ind] = 1
 pf += 1
ans.append([lis[:], ind, change])
print('frames\t'+' '.join(map(str,pages)))
for i in range(frames):
 print(str(i+1)+':', end='\t')
 for temp in range(n):
 if ans[temp][0][i]==None:
print(end=' ')
elif temp+1<n and ans[temp+1][2] and ans[temp+1][1]==i:
 print('\033[31m{}\033[0m'.format(ans[temp][0][i]), end=' ')
 else:
 print(ans[temp][0][i], end=' ')
print()
print('number of page faults:', str(pf-1))
