import sys

input = sys.stdin.readline

n = int(input())
dp = {0:0, 1:1, 2:1}
def fibo(i):
    if i not in dp:
        if i % 2 == 0:
            dp[i] = (fibo(i//2) * (fibo(i//2) + 2 * fibo(i//2 - 1))) % 1000000007
        else:
            dp[i] = (fibo(i//2) ** 2 + fibo(i//2 + 1) ** 2) % 1000000007
    return dp[i]

print(fibo(n))