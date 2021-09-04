import sys

a = int(sys.stdin.readline())
o = sys.stdin.readline().split()
s=[]
ans = [-1]*1000002
s.append(0)
for i in range(1,a):
    while len(s) != 0 and int(o[i])>int(o[s[len(s)-1]]):
        ans[s[len(s)-1]] = o[i]
        s.pop()
    s.append(i)
for i in range(a):
    print(ans[i], end = ' ')