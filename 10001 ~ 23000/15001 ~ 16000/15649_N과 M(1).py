import sys
n,m = map(int,sys.stdin.readline().split())
arr=[]
for i in range(1,n+1):
    arr.append(i)
check=[0]*n
ans = []
a=0
def dfs(a,n,m):
    if a==m:
        for i in ans:
            print(i,end = ' ')
        print('')
        return
    for i in range(n):
        if(check[i]==1):
            continue
        check[i] = 1
        ans.append(arr[i])
        dfs(a+1,n,m)
        ans.pop()
        check[i] = False

dfs(0,n,m)
