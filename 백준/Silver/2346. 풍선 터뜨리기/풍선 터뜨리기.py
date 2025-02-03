import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
input_arr = list(map(int, input().split()))

balloon = deque()
for i, num in enumerate(input_arr):
    balloon.append((num, i))

answer = []
while True:
    rotation, idx = balloon.popleft()
    answer.append(str(idx+1))
    if not balloon:
        break

    if rotation > 0:
        rotation -= 1
        for _ in range(rotation):
            balloon.append(balloon.popleft())
    else:
        for _ in range(-rotation):
            balloon.appendleft(balloon.pop())
    
print(' '.join(answer))