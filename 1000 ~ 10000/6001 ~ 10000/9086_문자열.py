import sys
n = int(sys.stdin.readline())
for _ in range(n):
    x = sys.stdin.readline().rstrip()
    print(f'{x[0]}{x[-1]}')