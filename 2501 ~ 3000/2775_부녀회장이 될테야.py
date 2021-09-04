import sys
ans = 1
a=int(sys.stdin.readline())
for i in range(a):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    list = [[0 for col in range(15)] for row in range(15)]
    for i in range(n):
        list[0][i] = i+1
    for i in range(1,k+1):
        list[i][0] = 1
    for i in range(1,k+1):
        for j in range(1,n):
            list[i][j] = list[i-1][j]+list[i][j-1]
    print(list[k][n-1])