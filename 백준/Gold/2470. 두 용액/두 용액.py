import sys

input = sys.stdin.readline

n = int(input())
features = list(map(int, input().split()))
features.sort()

left = 0
right = n-1

min_diff = float('inf')
answer = [0, 0]
while left < right:
    diff = features[left] + features[right]
    if min_diff > abs(diff):
        min_diff = abs(diff)
        answer = [features[left], features[right]]
    
    if diff > 0:
        right -= 1
    else:
        left += 1

print(*answer)