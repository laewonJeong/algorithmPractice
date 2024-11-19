import sys

while(True):
    try:
        n = int(sys.stdin.readline())
        dp = []
        dp.append(1)
        dp.append(3)
        dp.append(5)
        if n>=3:
            for i in range(3,n):
                dp.append(dp[i-1]+dp[i-2]*2)
        #print(dp)
        if n==0:
            print(1)
        else:
            print(dp[n-1])
    except:
        break