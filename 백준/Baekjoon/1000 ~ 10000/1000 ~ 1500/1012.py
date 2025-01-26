import sys
t = int(sys.stdin.readline())
g={}
def dfs(g,c,i):
    c[i] = 1
    for i in g[i]:
        if c[i] == 1:
            continue
        dfs(g,c,i)
for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    arr = [[0]*m for i in range(n)]
    for i in range(k):
        u,v = map(int,sys.stdin.readline().split())
        arr[v][u] =1
    c = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                g[m*i+j] = []
    for i in range(len(arr)):
        c=0
        if i == len(arr)-1:
            c=1
        for j in range(len(arr[i])):
            if c ==1 and j==len(arr[i])-1:
                c=0
                break
            if j == len(arr[i])-1:
                c=2
            if c == 1:
                if arr[i][j] == 1 and arr[i][j+1] == 1:
                    g[m*i+j].append(m*i+(j+1))
                    g[m*i+(j+1)].append(m*i+j)
                continue
            if c == 2:
                if arr[i][j] == 1 and arr[i+1][j]==1:
                    g[m*i+j].append(m*(i+1)+j)
                    g[m*(i+1)+j].append(m*i+j)
                continue
            if arr[i][j] == 1 and arr[i][j+1] == 1:
                g[m*i+j].append(m*i+(j+1))
                g[m*i+(j+1)].append(m*i+j)
            if arr[i][j] == 1 and arr[i+1][j]==1:
                g[m*i+j].append(m*(i+1)+j)
                g[m*(i+1)+j].append(m*i+j)
    check ={}
    cnt = 0
    for i in g:
        check[i] = 0
    for i in g:
        if check[i] == 0:
            dfs(g,check,i)
            cnt+=1
    print(cnt)
    check.clear()
    g.clear()
