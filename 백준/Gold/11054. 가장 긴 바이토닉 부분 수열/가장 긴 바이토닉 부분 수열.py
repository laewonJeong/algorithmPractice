import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
dp1 = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

answer = 0
for i in range(n):
    answer = max(answer, dp[i] + dp1[i] - 1)

print(answer)