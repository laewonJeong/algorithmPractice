import sys
input = sys.stdin.readline

n = int(input())
ball = 1

for _ in range(n):
    a, b = map(int, input().split())
    if a == ball:
        ball = b
    elif b == ball:
        ball = a

print(ball)