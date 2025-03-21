import bisect
import sys

input = sys.stdin.readline

n = int(input())
features = list(map(int, input().split()))
features.sort()

diff = float('inf')
answer = [0, 0]
for i in range(n):
    pos= bisect.bisect_left(features, -features[i])
    if pos != n:
        if pos != i and diff > abs(features[i] + features[pos]):
            diff = abs(features[i] + features[pos])
            answer = [features[i], features[pos]]
        if pos-1 != i and diff > abs(features[i] + features[pos-1]):
            diff = abs(features[i] + features[pos-1])
            answer = [features[i], features[pos-1]]
    else:
        if pos-1 != i and diff > abs(features[i] + features[pos-1]):
            diff = abs(features[i] + features[pos-1])
            answer = [features[i], features[pos-1]]

print(*sorted(answer))