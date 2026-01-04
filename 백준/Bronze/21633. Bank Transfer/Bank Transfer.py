import sys

k = int(sys.stdin.readline())
ans = k * 0.01 + 25
ans = max(100, ans)
ans = min(2000, ans)

print(f'{ans:.2f}')