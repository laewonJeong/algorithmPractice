import sys

people = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

answer_t = 0
for size in sizes:
    if size % t == 0:
        answer_t += size//t
    else:
        answer_t += size//t + 1
    
print(answer_t)
print(people//p, people%p)