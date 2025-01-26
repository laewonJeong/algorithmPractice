import sys
n = int(sys.stdin.readline())
for _ in range(n):
    dp=[1,2,4]
    x = int(sys.stdin.readline())
    for i in range(3,x):
        dp.append(dp[i-3]+dp[i-2]+dp[i-1])
    print(dp[x-1])
    dp.clear()