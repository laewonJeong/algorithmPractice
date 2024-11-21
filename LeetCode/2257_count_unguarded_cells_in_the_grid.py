class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        board = [[0] * n for _ in range(m)]
        
        for i, j in guards:
            board[i][j] = 'G'
        
        for i, j in walls:
            board[i][j] = 'W'
        
        moves = [[1,0], [0,1],[-1,0],[0,-1]]
        
        for i, j in guards:
            for move in moves:
                x, y = i, j
                while True:
                    x += move[0]
                    y += move[1]

                    if 0<=x<m and 0<=y<n and (board[x][y] == 0 or board[x][y] == -1):
                        board[x][y] = -1
                    else:
                        break

        answer = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    answer += 1
        
        return answer
