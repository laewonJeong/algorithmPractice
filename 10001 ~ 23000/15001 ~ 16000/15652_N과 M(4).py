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
        if check[i] == 1:
            continue
        ans.append(arr[i])
        dfs(a+1,n,m)
        ans.pop()
        check[i] = 1
        for j in range(i+1 , n):
            check[j] = 0
dfs(0,n,m)
