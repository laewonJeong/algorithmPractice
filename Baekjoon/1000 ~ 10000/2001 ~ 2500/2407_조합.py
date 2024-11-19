import sys

def com(n,r):
    arr=[[0]*102 for i in range(102)]
    for i in range(n+1):
        for j in range(r+1):
            if i==j or j==0:
                arr[i][j]=1
            else:
                arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
    return arr[n][r]

n,r = map(int,sys.stdin.readline().split())
print(com(n,r))