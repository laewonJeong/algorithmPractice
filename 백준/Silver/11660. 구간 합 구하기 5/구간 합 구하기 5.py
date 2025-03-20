import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        elif j == 0:
            board[i][j] += board[i-1][-1]
        else:
            board[i][j] += board[i][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    
    answer = 0
    for i in range(x1, x2+1):
        if i == 0:
            if y1 == 0:
                answer += board[i][y2]
            else:
                answer += board[i][y2] - board[i][y1-1]
        else:
            if y1 == 0:
                answer += board[i][y2] - board[i-1][-1]
            else:
                answer += board[i][y2] - board[i][y1 -1]

    print(answer)