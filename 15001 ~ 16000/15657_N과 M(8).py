import sys
arr1=[]
def dfs(a,idx,n,m):
    if a == m:
        print(' '.join(map(str, arr1)))
        return
    for i in range(idx,n):
        arr1.append(arr[i])
        dfs(a+1,i,n,m)
        arr1.pop()

n,m = map(int,sys.stdin.readline().split())
arr=[]
a = sys.stdin.readline().split()
for i in a:
    arr.append(int(i))
arr.sort()
dfs(0,0,n,m)