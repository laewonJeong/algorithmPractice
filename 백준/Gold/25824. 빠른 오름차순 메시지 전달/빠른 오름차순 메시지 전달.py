import sys
from collections import deque

input = sys.stdin.readline

answer = float('inf')
def dfs(graph, now, visited, path, distance):
    global answer
    if (now == 10 or now == 11) and False not in visited:
        answer = min(answer, distance)
        return

    for next_vertex, d in graph[now]:
        if not visited[next_vertex]:
            visited[next_vertex] = True
            path.append(next_vertex)

            dfs(graph, next_vertex, visited, path, distance+d)

            path.pop()
            visited[next_vertex] = False
    
idx = [[0,1,2,3], [0,1,2,3], [2,3,4,5], [2,3,4,5], [4,5,6,7], [4,5,6,7], [6,7,8,9], [6,7,8,9], [8,9,10,11], [8,9,10,11], [10,11], [10,11]]
graph = [[] for _ in range(12)]

for i in range(12):
    edges = list(map(int, input().split()))

    for j in range(idx[i][0], idx[i][-1]+1):
        if edges[j] != 0:
            graph[i].append([j,edges[j]])


visited = [False] * 12
visited[0] = True
dfs(graph, 0, visited, [0], 0)

visited = [False] * 12
visited[1] = True
dfs(graph, 1, visited, [1], 0)

print(answer)