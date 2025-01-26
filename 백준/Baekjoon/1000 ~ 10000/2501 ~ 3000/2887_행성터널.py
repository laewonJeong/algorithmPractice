import sys

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, a, b):
    A = find(parent, a)
    B = find(parent, b)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B
star = int(sys.stdin.readline())
parent = [0] * (star)
edges = []
result = 0
starLocation =[]
for i in range(star):
    parent[i] = i
for _ in range(star):
    x,y,c = map(int,sys.stdin.readline().split())
    starLocation.append([x,y,c,_])
for i in range(3):
    starLocation.sort(key=lambda x:x[i])
    for j in range(1,star):
        edges.append([abs(starLocation[j][i]-starLocation[j-1][i]),starLocation[j-1][3],starLocation[j][3]])

edges = sorted(edges)
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)
