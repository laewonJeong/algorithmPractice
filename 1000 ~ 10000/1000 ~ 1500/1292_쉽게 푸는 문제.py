import sys
n,m=map(int,input().split())
arr = []
for i in range(101):
    for j in range(i):
        arr.append(i)
sum=0
for i in range(n-1,m):
    sum += arr[i]
print(sum)