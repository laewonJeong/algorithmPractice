import sys
from collections import Counter
n=int(sys.stdin.readline())
arr=[]
ans=[]
for i in range(n):
    arr.append(sys.stdin.readline().rstrip())
a = Counter(arr)
max = -10**9
for i in a:
    if a[i]>max:
        max = a[i]
for i in a:
    if a[i] == max:
        ans.append(i)
ans = sorted(ans)
print(ans[0])