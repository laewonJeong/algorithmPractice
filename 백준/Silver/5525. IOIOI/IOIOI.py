import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

ioi = 'IO' * n + 'I'

answer = 0
for i in range(m):
    if s[i:].startswith(ioi):
        answer += 1

print(answer)