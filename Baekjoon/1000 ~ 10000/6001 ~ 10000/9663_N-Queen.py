import sys
def promising(i):
    for k in range(i):
        if col[k] == col[i]:
            return 0
        if abs(col[i] - col[k]) == i-k:
            return 0
    return 1
def nqueens(i):
    global cnt
    if i==n:
        cnt+=1
    else:
        for j in range(n):
            col[i]=j
            if promising(i):
                nqueens(i+1)

n=int(sys.stdin.readline())
col=[0]*n
cnt=0
nqueens(0)
print(cnt)