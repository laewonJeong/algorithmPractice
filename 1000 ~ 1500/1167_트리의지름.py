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
else:
    temp=[]
    temp1=[]
    for _ in range(n):
        s=sys.stdin.readline().split()
        for i in range(len(s)):
            if i%2==1:
                if s[i] != '-1':
                    tree[int(s[0])].append([int(s[i]),int(s[i+1])])
    check=[0] * (n+1)
    dfs(check,1,0)
    start_node = temp.index(max(temp))
    check1=[0]*(n+1)
    temp.clear()
    dfs(check1,temp1[start_node],0)
    print(max(temp))
