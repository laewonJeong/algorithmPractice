import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
num_seq = list(map(int, input().split()))
num_seq.sort()

visited = defaultdict(bool)
check = set()

def dfs(now, m, seq):
    if now == m:
        seq_tuple = tuple(seq)
        if seq_tuple not in check:
            check.add(seq_tuple)
            print(' '.join(map(str, seq)))
    for i, num in enumerate(num_seq):
        if not visited[i]:
            visited[i] = True
            dfs(now+1, m, seq + [num])
            visited[i] = False

dfs(0, m, [])