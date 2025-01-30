import sys

n = int(sys.stdin.readline())

dp = [float('inf') for _ in range(n+1)]

dp[0] = 0
if n >= 2:
    dp[2] = 1
if n >= 5:
    dp[5] = 1

for i in range(3, n+1):
    if i >= 2:
        dp[i] = min(dp[i], dp[i-2]+1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i-5]+1)

if dp[n] == float('inf'):
    print(-1)
else:
    print(dp[n])