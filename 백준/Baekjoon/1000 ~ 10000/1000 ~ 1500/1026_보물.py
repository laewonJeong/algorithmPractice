import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
arr1 = sys.stdin.readline().split()
arr = list(map(int,arr))
arr1 = list(map(int,arr1))
arr = sorted(arr, reverse=True)
arr1 = sorted(arr1)
ans = 0
for i in range(n):
    ans+= arr[i]*arr1[i]
print(ans)