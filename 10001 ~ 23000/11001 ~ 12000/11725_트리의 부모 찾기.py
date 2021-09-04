import sys
from collections import deque
check={}
def bfs(graph,start):
    check[start] = True
    q = deque()
    q1 = deque()
    q.append(start)
    q1.append(0)
    result =[0]*(n+1)
    while q:
        node = q.popleft()
        p_node = q1.popleft()
        result[node]=p_node
        for edge in graph[node]:
            if edge not in check:
                q.append(edge)
                q1.append(node)
                check[edge]=True
    return result
n = int(sys.stdin.readline())
tree = [[] for i in range(n+1)]
for _ in range(n-1):
    s,d = map(int,sys.stdin.readline().split())
    tree[s].append(d)
    tree[d].append(s)
a = bfs(tree,1)
for i in range(2,len(a)):
    print(a[i])