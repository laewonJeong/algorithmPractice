import sys
def e(m):
    a=[0]*(m+1)
    for i in range(2,m+1):
        a[i]=i
    k=int(m**0.5)
    for i in range(2,k+1):
        if a[i]==0:
            continue
        else:
            for j in range(i+i,m+1,i):
                a[j]=0
    b=m//2
    c=b
    for _ in range(10000):
        if a[b]!=0 and a[c]!=0:
            print(b,c)
            break
        b-=1
        c+=1
n = int(sys.stdin.readline())
for _ in range(n):
    o = int(sys.stdin.readline())
    e(o)