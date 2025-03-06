import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_seq = list(map(int, input().split()))

num_seq.sort()
check = set()

def dfs(now, m, before_seq, seq):
    if now == m:
        seq_tuple = tuple(seq)
        if seq_tuple not in check:
            check.add(seq_tuple)
            print(' '.join(map(str, seq)))
        return

    for num in num_seq:
        if not seq:
            dfs(now + 1, m, num, [num])
        elif before_seq <= num:
            dfs(now + 1, m, num, seq + [num])

dfs(0, m, 0, [])