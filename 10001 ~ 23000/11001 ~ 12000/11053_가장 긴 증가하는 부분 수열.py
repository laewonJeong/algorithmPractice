import sys
n = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
arr = list(map(int,arr))
dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))