import sys

input = sys.stdin.readline

n = int(input())

sequence = list(map(int, input().split()))
dp = sequence[:]
for i in range(1, n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j] + sequence[i])

print(max(dp))