import sys
a = int(sys.stdin.readline())
ans = []
while a>1:
    for i in range(2,10000000):
        if a % i == 0:
            a = a//i
            ans.append(i)
            break
ans = sorted(ans)
for i in ans:
    print(i)