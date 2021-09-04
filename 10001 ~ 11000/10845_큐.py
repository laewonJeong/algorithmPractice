from collections import deque
import sys

n=int(sys.stdin.readline())
d=deque()
for i in range(n):
    cmd = sys.stdin.readline().split()
    if 'push' in cmd:
        d.append(int(cmd[1]))
    elif 'pop' in cmd:
        if(len(d) != 0):
            print(d.popleft())
        else:
            print(-1)
    elif 'size' in cmd:
        print(len(d))
    elif 'empty' in cmd:
        if(len(d) == 0):
            print(1)
        else:
            print(0)
    elif 'front' in cmd:
        if(len(d) != 0):
            print(d[0])
        else:
            print(-1)
    elif 'back' in cmd:
        if(len(d) != 0):
            print(d[-1])
        else:
            print(-1)


