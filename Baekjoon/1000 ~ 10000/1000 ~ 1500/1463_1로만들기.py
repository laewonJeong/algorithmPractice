import sys

def min(a,b):
    if a<b:
        return a
    else:
        return b

a=int(sys.stdin.readline())
dp = []
for i in range(a+1):
    if i == 1 or i==0:
        dp.append(0)
        continue
    dp.append(dp[i-1]+1)
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
#print(dp)
print(dp[a])