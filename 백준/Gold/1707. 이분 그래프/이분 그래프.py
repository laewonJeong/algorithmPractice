import sys
from collections import deque

input = sys.stdin.readline


def is_bipartite(graph, n):
    color = [-1] * n

    for i in range(n):
        if color[i] != -1:
            continue
    
        q = deque([i])

        while q:
            vertex = q.popleft()

            for next_v in graph[vertex]:
                if color[next_v] == -1:
                    color[next_v] = 1 if color[vertex] == 0 else 0
                    q.append(next_v)
                elif color[next_v] == color[vertex]:
                    return False 
    return True


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        v, e = map(int, input().split())
        graph = [[] for _ in range(v)]

        for _ in range(e):
            v1, v2 = map(int, input().split())
            graph[v1-1].append(v2-1)
            graph[v2-1].append(v1-1)
        
        print("YES" if is_bipartite(graph, v) else "NO")
