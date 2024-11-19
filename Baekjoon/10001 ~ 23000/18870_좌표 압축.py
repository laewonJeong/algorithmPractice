import sys
n = int(sys.stdin.readline())
a = sys.stdin.readline().split()
r=[]
d={}
ans =[]
for i in a:
    r.append(int(i))
sr = sorted(r)
x=0
for i in range(len(sr)):
    if sr[i] not in d:
        d[sr[i]] = x
        x+=1
for i in r:
    print(d[i],end=' ')