import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n, r, query = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

subtree_size = [0] * (n + 1)
visited = [False] * (n + 1)

def dfs(r):
    visited[r] = True
    subtree_size[r] = 1

    for next in graph[r]:
        if not visited[next]:
            dfs(next)
            subtree_size[r] += subtree_size[next]

dfs(r)

for _ in range(query):
    vertex = int(input())
    print(subtree_size[vertex])