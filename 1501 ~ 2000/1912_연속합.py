import sys
n = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
arr = list(map(int,arr))
dp=[0]*1
dp[0] = arr[0]
for i in range(n-1):
    dp.append(max(dp[i]+arr[i+1],arr[i+1]))
print(max(dp))