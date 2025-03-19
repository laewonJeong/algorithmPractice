import sys

input = sys.stdin.readline

n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

count = 0
def dfs(x, y, state):
    global count
    if x == n-1 and y == n-1:
        count += 1
        return

    if state == 0:
        if y == n-1:
            return
        if 0 <= y + 1 < n and board[x][y+1] == 0:
            dfs(x, y+1, 0)
        if 0 <= x + 1 < n and 0 <= y + 1 < n and board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)
   
    elif state == 1:
        if x == n-1:
            return
        if 0 <= x + 1 < n and board[x+1][y] == 0:
            dfs(x+1, y, 1)
        if 0 <= x + 1 < n and 0 <= y + 1 < n and board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)
   
    else:
        if 0 <= y + 1 < n and board[x][y+1] == 0:
            dfs(x, y+1, 0)
        if 0 <= x + 1 < n and board[x+1][y] == 0:
            dfs(x+1, y, 1)
        if 0 <= x + 1 < n and 0 <= y + 1 < n and board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)

dfs(0,1,0)
print(count)