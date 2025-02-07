import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = []

for _ in range(n):
    board.append(list(input().rstrip()))


moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = []

for i in range(n):
    for j in range(n):
        if board[i][j] == '1':
            q = deque([(i, j)])
            board[i][j] = '0'
            cnt = 0

            while q:
                x, y = q.popleft()
                cnt+=1

                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == '1':
                        q.append((nx, ny))
                        board[nx][ny] = '0'

            answer.append(cnt)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)