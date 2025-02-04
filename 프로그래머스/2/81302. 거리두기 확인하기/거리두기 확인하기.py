def check_can(place, i, j, n, m):
    moves_one = [[1,0], [-1,0], [0,1], [0,-1]]
    moves_two = [[0, 2], [0, -2], [2, 0], [-2, 0]]
    moves_dia = [[1, 1], [1,-1], [-1,-1], [-1,1]]
    
    for move in moves_one:
        nx = i+move[0]
        ny = j+move[1]
        if 0 <= nx < n and 0 <= ny < m and place[nx][ny] == 'P':
            #print(i, j, nx, ny)
            return False
                        
    for move in moves_two:
        nx = i+move[0]
        ny = j+move[1]
                        
        px = i + move[0]//2
        py = j + move[1]//2
                        
        if 0 <= nx < n and 0 <= ny < m and place[nx][ny] == 'P' and place[px][py] != 'X':
            #print(i, j, nx, ny)
            return False
        
    for move in moves_dia:
        nx = i+move[0]
        ny = j+move[1]
        
        px1 = i+move[0]
        py1 = j
        
        px2 = i
        py2 = j+move[1]
        
        if 0 <= nx < n and 0 <= ny < m and place[nx][ny] == 'P' and not (place[px1][py1] == 'X' and place[px2][py2] == 'X'):
            return False
        
    return True
    
def solution(places):
    answer = []
    n, m = 5, 5
    
    for place in places:
        check = True
        for i in range(n):
            for j in range(m):
                if place[i][j] == 'P' and check:
                    check = check_can(place, i, j, n, m)
                    
        if check: answer.append(1)
        else: answer.append(0)

    return answer