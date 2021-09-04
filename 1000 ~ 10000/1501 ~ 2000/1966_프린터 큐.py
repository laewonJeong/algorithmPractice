import sys
from collections import deque
d=deque()
seq=deque()
count = 0
ans = 0
check = 0
num = int(sys.stdin.readline())
for _ in range(num):
    a,b = map(int,sys.stdin.readline().split())
    t = sys.stdin.readline().split()
    for i in range(len(t)):
        d.append(int(t[i]))
        seq.append(i)
    while(b in seq):
        check = 0
        for i in range(len(d)):
            if d[0]<d[i]:
                t = d[0]
                t1 = seq[0]
                d.popleft()
                d.append(t)
                seq.popleft()
                seq.append(t1)
                check =1
        if check == 0:
            d.popleft()
            if seq[0] == b:
               seq.popleft()
               count+=1
               ans = count
            else:
               seq.popleft()
               count+=1
    print(ans)
    seq.clear()
    d.clear()
    count = 0