import sys
n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    w = map(int, sys.stdin.readline().split())
    h = list(map(int, sys.stdin.readline().split()))

    answer = sum(w) * 2 + sum(h) * 2
    for i in range(x - 1):
        answer -= 2 * min(h[i], h[i + 1])

    print(answer)