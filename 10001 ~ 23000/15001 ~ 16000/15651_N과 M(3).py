import sys

n,m = map(int,sys.stdin.readline().split())
check=[0]*n
arr=[]
for i in range(1,n+1):
    arr.append(i)
ans = []
a = 0
def dfs(a,n,m):
    if a==m:
        for i in ans:
            print(i,end=' ')
        print('')
        return
    for i in range(n):
        check[i] =1
        ans.append(arr[i])
        dfs(a+1,n,m)
        ans.pop()

dfs(0,n,m)