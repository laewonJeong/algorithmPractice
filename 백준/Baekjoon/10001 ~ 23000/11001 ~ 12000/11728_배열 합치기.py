import sys
n,m = map(int,sys.stdin.readline().split())
arr=[]
x=sys.stdin.readline().split()
y=sys.stdin.readline().split()
for i in x:
    arr.append(int(i))
for i in y:
    arr.append(int(i))
arr = sorted(arr)
for i in arr:
    print(i,end=' ')