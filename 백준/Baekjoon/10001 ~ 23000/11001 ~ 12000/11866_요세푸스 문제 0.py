from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())
d=deque()
d1=deque()
for i in range(1,n+1):
    d.append(i)
d.appendleft(0)
#print(d)
cnt =0
i=0
while len(d1) != n:
    i+=1
    cnt +=1
    if i > n:
        i = 1
    if cnt == m and d[i] == i:
            d1.append(i)
            d[i] = 0
            cnt = 0
    elif d[i] == 0:
        cnt-=1

for i in range(len(d1)):
    if(len(d1) == 1):
        print(f'<{d1[0]}>')
        break
    if i ==0:
        print(f'<{d1[i]},',end = ' ')
    elif i == len(d1)-1:
        print(f'{d1[i]}>',end = ' ')
    else:
        print(f'{d1[i]},',end = ' ')