import sys
import bisect

input = sys.stdin.readline

n = int(input())
solvent = list(map(int, input().split()))

min_sum_solvent = float('inf')
min_answer, max_answer = 0, 0

for i in range(n):
    target = -solvent[i]
    j = bisect.bisect_left(solvent, target)

    for k in (j - 1, j, j + 1):
        if k == i or k < 0 or k >= n:
            continue
        sum_solvent = abs(solvent[i] + solvent[k])
        if sum_solvent < min_sum_solvent:
            min_sum_solvent = sum_solvent
            min_answer, max_answer = solvent[i], solvent[k]

print(f'{min(min_answer, max_answer)} {max(min_answer, max_answer)}')