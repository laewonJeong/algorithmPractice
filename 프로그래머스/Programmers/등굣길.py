def solution(m, n, puddles):
    dp = [[1 for _ in range(m)] for _ in range(n)]
    
    for x, y in puddles:
        dp[y-1][x-1] = 0

    for i in range(n):
        for j in range(m):
            if dp[i][j] == 0: continue
            
            elif i == 0 and j != 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0 and i != 0:
                dp[i][j] = dp[i-1][j]
            elif i != 0 and j != 0:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

    return dp[-1][-1] % 1000000007
