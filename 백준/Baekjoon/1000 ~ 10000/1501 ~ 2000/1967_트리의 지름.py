import sys
sys.setrecursionlimit(10**9)
def dfs(check,i,n):
    result = n
    temp.append(n)
    temp1.append(i)
    check[i] = 1
    for j,k in tree[i]:
        y = j
        a=result + k
        if check[y]==0:
            dfs(check,y,a)

n = int(sys.stdin.readline())
tree=[[] for i in range(n+1)]

if n == 1:
    print(0)
elif n ==2:
    temp=[]
    temp1=[]
    for _ in range(n-1):
        s,d,w = map(int,sys.stdin.readline().split())
        tree[s].append([d,w])
        tree[d].append([s,w])
    check=[0] * (n+1)
    dfs(check,1,0)
    print(max(temp))
else:
    temp=[]
    temp1=[]
    for _ in range(n-1):
        s,d,w = map(int,sys.stdin.readline().split())
        tree[s].append([d,w])
        tree[d].append([s,w])
    check=[0] * (n+1)
    dfs(check,1,0)
    start_node = temp.index(max(temp))
    check1=[0]*(n+1)
    temp.clear()
    dfs(check1,temp1[start_node],0)
    print(max(temp))
