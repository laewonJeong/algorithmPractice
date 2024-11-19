import sys
from collections import Counter
s=[]
n=int(sys.stdin.readline())
for _ in range(n):
    m=int(sys.stdin.readline())
    for _ in range(m):
        cloth, a = sys.stdin.readline().split()
        s.append(a)
    ans = Counter(s)
    result = 1
    for i in ans:
        result *= ans[i]+1
    print(result-1)
    result=0
    s.clear()
    ans.clear()