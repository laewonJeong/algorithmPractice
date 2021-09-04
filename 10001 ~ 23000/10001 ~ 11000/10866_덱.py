import sys
from collections import deque

d = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if 'push_back' in cmd:
        d.append(int(cmd[1]))
    elif 'push_front' in cmd:
        d.appendleft(int(cmd[1]))
    elif 'pop_front' in cmd:
        if len(d) != 0:
            print(d.popleft())
        else:
            print(-1)
    elif 'pop_back' in cmd:
        if len(d) != 0:
            print(d.pop())
        else:
            print(-1)
    elif 'size' in cmd:
        print(len(d))
    elif 'empty' in cmd:
        if len(d) != 0:
            print(0)
        else:
            print(1)
    elif 'front' in cmd:
        if len(d) != 0:
            print(d[0])
        else:
            print(-1)
    elif 'back' in cmd:
        if len(d) != 0:
            print(d[-1])
        else:
            print(-1)