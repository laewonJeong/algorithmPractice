from collections import deque
import sys

n=int(sys.stdin.readline())
d=deque()
for i in range(1,n+1):
    d.append(i)
while len(d) != 1:
    d.popleft()
    d.append(d[0])
    d.popleft()
print(d[0])