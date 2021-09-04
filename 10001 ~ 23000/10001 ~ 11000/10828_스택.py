import sys

s= []
a=int(input())
for i in range(a):
    cmd = sys.stdin.readline().split()
    if 'push' in cmd:
        s.append(cmd[1])
    elif 'top' in cmd:
        if len(s)!=0:
            print(int(s[len(s)-1]))
        else:
            print(-1)
    elif 'pop' in cmd:
        if len(s)!=0:
            print(s[len(s)-1])
            s.pop()
        else:
            print(-1)
    elif 'size' in cmd:
        print(len(s))
    elif 'empty' in cmd:
        if len(s)!=0:
            print(0)
        else:
            print(1)