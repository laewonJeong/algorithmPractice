def check_mine(r,c,a,x,y):
    result = 0
    for i in range(len(x)):
        if r+x[i] >= 0 and r+x[i] < len(a) and c+y[i] >= 0 and c+y[i] < len(a[0]):
            if(a[r+x[i]][c+y[i]] == '*'):
                result += 1
    return str(result)
        
x = [-1, 0 ,1,-1, 1, -1, 1, 0]
y = [-1,-1,-1, 0, 0, 1, 1, 1]
while(1):
    r,c = map(int,input().split())
    if r == 0 and c == 0:
        break
    mine = []
    for i in range(r):
        mine.append([])
        a = input()
        for dot in a:
            mine[i].append(dot)
    for i in range(r):
        for j in range(c):
            if mine[i][j] == '.':
                mine[i][j] = check_mine(i,j,mine,x,y)
    for i in mine:
        for j in i:
            print(j,end='')
        print()
            