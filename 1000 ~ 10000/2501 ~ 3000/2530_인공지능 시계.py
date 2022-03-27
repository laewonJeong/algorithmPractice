import sys
h,m,s = map(int,sys.stdin.readline().split())
s1 = int(sys.stdin.readline())
for i in range(1,s1+1):
    s+=1
    if s == 60:
        s=0
        m+=1
        if m == 60:
            m=0
            h+=1
            if h == 24:
                h=0
print(h,m,s)
