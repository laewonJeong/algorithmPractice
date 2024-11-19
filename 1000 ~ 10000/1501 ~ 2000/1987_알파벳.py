import sys

nr =[-1,0,1,0]
nc =[0,-1,0,1]
def dfs(i,j,ans,r,c):
    global max
    if ans > max:
        max = ans
    for k in range(4):
        nextr = i+nr[k]
        nextc = j+nc[k]
        if(0<=nextr<r) and (0<=nextc<c) and (C[board[nextr][nextc]] == [0]):
            C[board[nextr][nextc]] =1
            dfs(nextr,nextc,ans+1,r,c)
            C[board[nextr][nextc]] =[0]
r,c = map(int,sys.stdin.readline().split())
board = [list(map(lambda x: ord(x)-65,sys.stdin.readline())) for i in range(r)]
C = [[0] for j in range(26)]
max = 0
C[board[0][0]] = 1
dfs(0,0,1,r,c)
print(max)