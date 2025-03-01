import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())

maze = []

for _ in range(n):
    maze.append(list(input().rstrip()))

visited = [[False] * m for _ in range(n)]
moves = [[0,1],[0,-1],[1,0],[-1,0]]

q = deque([(1, 0, 0)])

while q:
    cnt, x, y = q.popleft()
    if x == n-1 and y == m-1:
        print(cnt)
        break

    for move in moves:
        nx = x+move[0]
        ny = y+move[1]

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maze[nx][ny] == '1':
            q.append((cnt+1, nx, ny))
            visited[nx][ny] = True