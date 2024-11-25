class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        want_result = [[1,2,3],[4,5,0]]
        visited = defaultdict(bool)

        for i in range(2):
            if 0 in board[i]:
                start_x = i
                start_y = board[i].index(0)
                break
        
        moves = [[0,1], [1, 0], [0,-1], [-1,0]]
        visited[tuple(board[0] + board[1])] = True
        q = deque([[start_x, start_y, 0, deepcopy(board)]])

        while q:
            x, y, cnt, now_board = q.popleft()
            if now_board == want_result:
                return cnt

            for move in moves:
                nx = x+move[0]
                ny = y+move[1]

                if 0 <= nx < 2 and 0 <= ny < 3:
                    now_board[x][y], now_board[nx][ny] = now_board[nx][ny], now_board[x][y]

                    if not visited[tuple(now_board[0] + now_board[1])]:
                        visited[tuple(now_board[0] + now_board[1])] = True
                        q.append([nx, ny, cnt + 1, deepcopy(now_board)])
                    
                    now_board[x][y], now_board[nx][ny] = now_board[nx][ny], now_board[x][y]

        return -1
