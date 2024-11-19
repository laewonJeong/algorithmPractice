import sys
ans = [0]*1000001
a=int(sys.stdin.readline())
dp = []
for i in range(a+1):
    if i == 1 or i==0:
        dp.append(0)
        continue
    dp.append(dp[i-1]+1)
    ans[i]=i-1
    if i%2==0 and dp[i]>dp[i//2]+1:
        dp[i] = dp[i//2]+1
        ans[i] = i//2
    if i%3==0 and dp[i]>dp[i//3]+1:
        dp[i] = dp[i//3]+1
        ans[i] = i//3

print(dp[a])
while(a!=0):
    print(a,end=' ')
    a = ans[a]