import sys

def binary_search(arr,k,n,m):
    while n<=m:
        mid = (n+m)//2
        cnt = 0
        for i in arr:
            cnt += i//mid
        if cnt >= k:
            n = mid+1
        else:
            m= mid-1
    return m
a,b = map(int,sys.stdin.readline().split())
max = 0
min = 0
list = []
for i in range(a):
    x=int(sys.stdin.readline())
    list.append(x)
    if max<x:
        max=x
print(binary_search(list,b,1,max))