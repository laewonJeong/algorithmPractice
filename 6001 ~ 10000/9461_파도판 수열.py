import sys

pado = [0] * 100
pado[0] = 1
pado[1] = 1
pado[2] = 1
n=int(sys.stdin.readline())
for _ in range(n):
    num = int(input())
    for i in range(3,num):
        if pado[i] ==0:
            pado[i]=pado[i-2]+pado[i-3]
    print(pado[num-1])