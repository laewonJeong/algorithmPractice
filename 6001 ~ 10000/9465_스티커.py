import sys

testcase = int(sys.stdin.readline())
for _ in range(testcase):
    sticker = [[] for i in range(2)]
    n = int(sys.stdin.readline())
    dp=[0]*n
    dp1=[0]*n
    for j in range(2):
        a = sys.stdin.readline().split()
        for i in a:
            sticker[j].append(int(i))
    if n == 1:
        print(max(sticker[0][0],sticker[1][0]))
    else:
        dp[0] = sticker[0][0]
        dp1[0] = sticker[1][0]
        dp[1] =sticker[1][0]+sticker[0][1]
        dp1[1] =  sticker[0][0]+sticker[1][1]
        for i in range(2,n):
            dp[i] = max(sticker[0][i]+dp1[i-2],sticker[0][i]+dp1[i-1])
            dp1[i] = max(sticker[1][i]+dp[i-2],sticker[1][i]+dp[i-1])
        print(max(dp[n-1],dp1[n-1]))