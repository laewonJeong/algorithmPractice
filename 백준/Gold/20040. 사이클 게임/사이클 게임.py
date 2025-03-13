import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
        
        
n, m = map(int, input().split())

parent = list(range(n))
cycle = False
answer = 0

for i in range(m):
    v1, v2 = map(int, input().split())
    
    if find(parent, v1) == find(parent, v2):
        if not cycle:
            cycle = True
            answer = i + 1
            break
    else:
        union(parent, v1, v2)

print(answer)