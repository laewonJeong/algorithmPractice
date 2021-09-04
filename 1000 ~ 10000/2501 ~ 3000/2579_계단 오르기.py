import sys
n = int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
if n ==1:
    print(arr[0])
elif n==2:
    print(sum(arr))
else:
    dp=[0]*3
    dp[0] = arr[0]
    dp[1] = (arr[0]+arr[1])
    dp[2] = (max(arr[0]+arr[2],arr[1]+arr[2]))
    for i in range(3,n):
         dp.append(max(dp[i-2]+arr[i],dp[i-3]+arr[i]+arr[i-1]))
    print(dp.pop())