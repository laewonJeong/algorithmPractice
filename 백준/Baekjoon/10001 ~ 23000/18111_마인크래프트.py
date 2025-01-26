import sys
n,m,b = map(int,sys.stdin.readline().split())
a=[]
at=922337203685477580
h=0
for i in range(n):
    a.append(sys.stdin.readline().split())
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])
x =b
for i in range(257):
    b=x
    t=0
    for j in a:
        for k in j:
            if k>i:
                t+=2*(k-i)
                b+=(k-i)
            elif i>k:
                t+=i-k
                b-=(i-k)
    if b<0:
        continue
    if t<=at:
        at = t
        h = i
print("{} {}".format(at,h))
