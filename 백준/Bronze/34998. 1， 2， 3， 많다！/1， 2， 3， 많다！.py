import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    x   = int(input())
    exp = input().strip()

    if '!' in exp or eval(exp) >= 10:
        print('!')
    else:
        print(eval(exp))