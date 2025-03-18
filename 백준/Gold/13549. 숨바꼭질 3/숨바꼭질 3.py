from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([(0, n)])
visited = [False] * 100001
visited[n] = True

while q:
    time, x = q.popleft()
    if x == k:
        print(time)
        break

    for nx in [x*2, x-1, x+1]:
        if 0 <= nx < 100001 and not visited[nx]:
            visited[nx] = True
            if nx == x*2:
                q.append((time, nx))
            else:
                q.append((time+1, nx))