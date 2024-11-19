import sys
a=int(sys.stdin.readline())
for i in range(a):
    b,c,d=map(int,sys.stdin.readline().split())
    k=1
    x=1
    for i in range(1,d+1):
        if x>b:
            x=1
            k+=1
        ans = x*100+k
        x+=1
    print(ans)