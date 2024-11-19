import sys
n = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
arr = list(map(int,arr))
arr = sorted(arr)
ans = 0
temp = 0
for i in arr:
    temp+=i
    ans+=temp
print(ans)
