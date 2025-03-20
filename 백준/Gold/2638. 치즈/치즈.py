import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]

            if 0 <= nx < n and 0 <= ny < m:
                
                if paper[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif paper[nx][ny] == 1:
                    visited[nx][ny] += 1

answer = 0

while True:
    answer += 1
    visited = [[0] * m for _ in range(n)]
    bfs(0, 0, visited)

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                paper[i][j] = 0

    if sum([sum(row) for row in paper]) == 0:
        break

print(answer)