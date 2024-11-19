import sys
n,m = map(int,sys.stdin.readline().strip().split())
w1=[]
v1=[]
for _ in range(n):
    w,v = map(int,sys.stdin.readline().strip().split())
    w1.append(w)
    v1.append(v)
dp=[[0 for x in range(m+1)] for x in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i ==0 or j==0:
            dp[i][j] = 0
        elif w1[i-1]<=j:
            dp[i][j] = max(dp[i-1][j],v1[i-1]+dp[i-1][j-w1[i-1]])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][m])