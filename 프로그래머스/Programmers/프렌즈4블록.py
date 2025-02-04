from collections import defaultdict

def can_bomb_loc(board, now_i, now_j, m, n, loc, now_block, check_loc):
    if now_block == 0:
        return loc
    
    check = [[[-1, 0], [-1, -1], [0, -1]], [[-1, 0], [-1, 1], [0, 1]], 
            [[0, -1], [1, 0], [1, -1]], [[0,1], [1,0], [1, 1]]]

    for c in check:
        temp = []
        for i, j in c:
            ni = now_i + i
            nj = now_j + j
            
            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == now_block:
                temp.append((ni, nj))
            else:
                break
        
        if len(temp) == 3:
            temp.append((now_i, now_j))
            for i, j in temp:
                if not check_loc[(i, j)]:
                    check_loc[(i,j)] = True
                    loc.append((i,j))
                    
    return loc
    
def solution(m, n, board):
    answer = 0
    new_board = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(m-1, -1, -1):
            new_board[i].append(board[j][i])

    while True:
        loc = []
        check_loc = defaultdict(bool)

        for i in range(n):
            for j in range(m):
                loc = can_bomb_loc(new_board,i,j, m, n, loc, new_board[i][j], check_loc)
        
        for i, j in loc:
            new_board[i][j] = -1
        
        for i in range(n):
            while -1 in new_board[i]:
                new_board[i].remove(-1)
                new_board[i].append(0)
                
        answer+=len(loc)
        
        if len(loc) == 0:
            break
        
    return answer
