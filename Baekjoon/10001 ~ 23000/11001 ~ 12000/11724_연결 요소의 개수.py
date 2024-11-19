import sys
sys.setrecursionlimit(10000)
a,b=map(int,input().split())
check = [0]*(a+1)
arr = [[0 for i in range(2)] for j in range(b)]
g = [[0 for i in range(a)] for j in range(a)]
c = 0
def dfs(a,n):
    check[a] =1
    for i in range(n):
        if check[i] == 1 or g[a][i] == 0:
            continue
        dfs(i,n)
for i in range(b):
    u,v = map(int,input().split())
    arr[i][0] = u
    arr[i][1] = v
for i in range(len(arr)):
    g[arr[i][0]-1][arr[i][1]-1]=1
    g[arr[i][1]-1][arr[i][0]-1]=1
for i in range(a):
    if check[i] == 0:
        dfs(i,a)
        c+=1
print(c)