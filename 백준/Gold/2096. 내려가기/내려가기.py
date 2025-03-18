import sys

input = sys.stdin.readline

n = int(input())

dp1 = [0, 0, 0]
dp2 = [0, 0, 0]

for _ in range(n):
    nums = (list(map(int, input().split())))
    dp1[0], dp1[1], dp1[2] = min(dp1[0], dp1[1]) + nums[0], min(dp1) + nums[1], min(dp1[1], dp1[2]) + nums[2]
    dp2[0], dp2[1], dp2[2] = max(dp2[0], dp2[1]) + nums[0], max(dp2) + nums[1], max(dp2[1], dp2[2]) + nums[2]

print(max(dp2), min(dp1))