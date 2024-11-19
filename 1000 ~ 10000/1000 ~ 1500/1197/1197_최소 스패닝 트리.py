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
v,e = map(int, sys.stdin.readline().split())
parent = [0] * (v+1)
edges = []
result = 0
for i in range(1, v+1):
    parent[i] = i
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges = sorted(edges)
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
print(result)