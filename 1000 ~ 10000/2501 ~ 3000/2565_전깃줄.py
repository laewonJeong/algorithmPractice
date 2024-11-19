import sys
n = int(sys.stdin.readline())
arr = [0]*502
dp = [1]*502

for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    arr[x] = y
for i in range(1,502):
    tmp =1
    for j in range(1,i+1):
        if arr[i] != 0:
        #print(arr[i],arr[j])
            if arr[i]>arr[j] and arr[j] != 0:
                tmp = max(tmp,dp[j]+1)
        #print(tmp)
    dp[i] = tmp
print(n-max(dp))
