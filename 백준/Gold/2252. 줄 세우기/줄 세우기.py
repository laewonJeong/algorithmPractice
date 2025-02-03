import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

in_degree = [0] * n
graph = [[] for _ in range(n)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1-1].append(v2-1)
    in_degree[v2-1] += 1

q = deque()
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)

answer = []
while q:
    vertex = q.popleft()
    print(vertex+1, end = ' ')
    for next_vertex in graph[vertex]:
        in_degree[next_vertex] -= 1
        if in_degree[next_vertex] == 0:
            q.append(next_vertex)