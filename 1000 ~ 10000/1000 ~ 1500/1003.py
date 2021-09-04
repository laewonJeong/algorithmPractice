import sys
n=int(sys.stdin.readline())
z=[]
o=[]
for _ in range(n):
    z.append(1)
    z.append(0)
    o.append(0)
    o.append(1)
    num=int(sys.stdin.readline())
    for i in range(2,num+1):
        o.append(o[i-1]+o[i-2])
        z.append(z[i-1]+z[i-2])
    print(z[num],o[num])
    z.clear()
    o.clear()