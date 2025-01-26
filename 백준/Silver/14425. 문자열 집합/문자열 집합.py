import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
s = defaultdict(bool)
answer = 0

for _ in range(n):
    s[sys.stdin.readline()] = True
    
for _ in range(m):
    if s[sys.stdin.readline()]:
        answer += 1

print(answer)