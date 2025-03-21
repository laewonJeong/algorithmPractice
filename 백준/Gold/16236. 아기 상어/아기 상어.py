import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

area = []
for i in range(n):
    area.append(list(map(int, input().split())))
    for j in range(n):
        if area[i][j] == 9:
            start = (i, j)
            area[i][j] = 0

def bfs(start, size):
    visited = [[0]*n for _ in range(n)]
    q = deque([start])
    visited[start[0]][start[1]] = 1
    eat = []
    while q:
        x, y = q.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]

            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] <= size and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    if 0 < area[nx][ny] < size:
                        eat.append((nx, ny, visited[nx][ny]-1))
    return eat

size = 2
eat = 0
time = 0
moves= [(0, 1), (0, -1), (1, 0), (-1, 0)]

while True:
    result = bfs(start, size)
    if not result:
        print(time)
        break
    result.sort(key=lambda x: (-x[2], -x[0], -x[1]))
    x, y, t = result.pop()
    time += t
    area[x][y] = 0
    eat += 1
    if eat == size:
        size += 1
        eat = 0
    start = (x, y)