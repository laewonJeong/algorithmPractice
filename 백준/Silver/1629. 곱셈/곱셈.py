import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    elif b % 2 == 0:
        return power(a, b//2) ** 2 % c
    else:
        return a * power(a, b//2) ** 2 % c

print(power(a, b))