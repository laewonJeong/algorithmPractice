import sys

n = int(sys.stdin.readline())
dp=[[0]*10 for i in range(102)]
dp[0][0] = 0
for i in range(1,10):
    dp[0][i] = 1
for i in range(1,100):
    dp[i][0] = dp[i-1][1]%1000000000
    for j in range(1,9):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1])%1000000000
    dp[i][9] = dp[i-1][8]%1000000000
print(sum(dp[n-1])%1000000000)
