import sys

t = int(sys.stdin.readline())
max_n = 1000000
dp = [0] * (max_n + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_n+1):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n] % 1000000009)