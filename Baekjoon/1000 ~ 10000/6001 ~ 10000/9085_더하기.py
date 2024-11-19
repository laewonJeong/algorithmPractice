import sys
n=int(input())
for _ in range(n):
    x=int(input())
    arr = sys.stdin.readline().split()
    arr = list(map(int,arr))
    print(sum(arr))