import sys
n = int(sys.stdin.readline())
arr=[0]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
dp=[0]*1
dp.append(arr[1])
if n>1:
    dp.append(arr[1]+arr[2])
for i in range(3,n+1):
    dp.append(max(dp[i-1],dp[i-3]+arr[i]+arr[i-1],dp[i-2]+arr[i]))
print(dp[n])