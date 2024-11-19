import sys
import math
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
parent = [0] * (star+1)
edges = []
result = 0
starLocation =[]
for i in range(1, star+1):
    parent[i] = i
for _ in range(star):
    x,y = map(float,sys.stdin.readline().split())
    starLocation.append([x,y])
for i in range(star):
    for j in range(star):
        if i == j:
            continue
        cost = math.sqrt((starLocation[j][0]-starLocation[i][0])**2 + (starLocation[j][1]-starLocation[i][1])**2)
        edges.append((cost,i+1,j+1))

edges = sorted(edges)
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print('%.2f' % result)
