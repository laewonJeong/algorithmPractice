import sys
from collections import deque

n = int(sys.stdin.readline())
apple = int(sys.stdin.readline())
temp = deque()
dq = deque()
board = [[0 for i in range(n+1)] for j in range(n+1)]
for _ in range(apple):
    r,c = map(int,sys.stdin.readline().split())
    board[r][c] = 1
cmd = int(sys.stdin.readline())
for _ in range(cmd):
    x,c = sys.stdin.readline().split()
    temp.append([int(x),c])
check = True
time = 0
second = temp[0][0]
dir = 'r'
i = 1
j= 1
dq.append([i,j])
while(check == True):
    if time == second:
        if temp[0][1] == 'D':
            if dir =='r':
                dir = 'd'
            elif dir == 'l':
                dir ='u'
            elif dir == 'u':
                dir = 'r'
            elif dir == 'd':
                dir = 'l'
        if temp[0][1] == 'L':
            if dir =='r':
                dir = 'u'
            elif dir == 'l':
                dir ='d'
            elif dir == 'u':
                dir = 'l'
            elif dir == 'd':
                dir = 'r'
        temp.popleft()
        if(len(temp)!=0):
            second = temp[0][0]
        #print(time)
        #print(dir)
    if dir == 'r':
        j+=1
        if j>n:
            check = False
            break
        if [i,j] in dq:
            check = False
            break
        dq.append([i,j])
        if(board[i][j] == 0):
            dq.popleft()
        else:
            board[i][j] =0
    if(dir == 'l'):
        j-=1
        if j<1:
            check = False
            break
        if [i,j] in dq:
            check = False
            break
        dq.append([i,j])
        if(board[i][j] == 0):
            dq.popleft()
        else:
            board[i][j] =0
    if(dir == 'u'):
        i-=1
        if i<1:
            check = False
            break
        if [i,j] in dq:
            check = False
            break
        dq.append([i,j])
        if(board[i][j] == 0):
            dq.popleft()
        else:
            board[i][j] =0
    if(dir == 'd'):
        i+=1
        if i>n:
            check = False
            break
        if [i,j] in dq:
            check = False
            break
        dq.append([i,j])
        if(board[i][j] == 0):
            dq.popleft()
        else:
            board[i][j] =0
    time +=1
print(time+1)