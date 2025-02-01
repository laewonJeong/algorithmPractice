def dfs(board, visited, n, m, x, y):
    moves = [[0,1],[0,-1],[1,0],[-1,0]]

    for move in moves:
        nx = x + move[0]
        ny = y + move[1]
        if 0 <= nx < n and 0 <=ny < m and not visited[nx][ny] and board[nx][ny] == 'X':
            visited[nx][ny] = True
            dfs(board, visited, n, m, nx, ny)

    
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        visited = [[False]*m for _ in range(n)]

        answer = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and board[i][j] == 'X':
                    answer += 1
                    visited[i][j] = True
                    dfs(board, visited, n, m, i, j)
            
        return answer