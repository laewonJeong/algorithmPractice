def check_mine(r,c,a,x,y):
    result = 0
    for i in range(len(x)):
        if r+x[i] >= 0 and r+x[i] < len(a) and c+y[i] >= 0 and c+y[i] < len(a[0]):
            if(a[r+x[i]][c+y[i]] == '*'):
                result += 1
    return str(result)
        
x = [-1, 0 ,1,-1, 1, -1, 1, 0]
y = [-1,-1,-1, 0, 0, 1, 1, 1]

n = int(input())
mine = []
game_mine = []
for i in range(n):
    mine.append([])
    a = input()
    for dot in a:
        mine[i].append(dot)
for i in range(n):
    game_mine.append([])
    a = input()
    for dot in a:
        game_mine[i].append(dot)

check = 0
for i in range(n):
    for j in range(n):
        if game_mine[i][j] == 'x':
            game_mine[i][j] = check_mine(i,j,mine,x,y)
            if mine[i][j] == '*':
                check = 1
if check == 1:
    for i in range(len(mine)):
        for j in range(len(mine[i])):
            if mine[i][j] == '*':
                game_mine[i][j] = '*'

for i in game_mine:
    for j in i:
        print(j,end='')
    print()