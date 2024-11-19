import sys
n=int(sys.stdin.readline())
arr = sys.stdin.readline().split()
arr = list(map(int,arr))
for i in range(1,n):
    if arr[i] == 1 and arr[i-1] != 0:
        arr[i] = arr[i-1]+1
print(sum(arr))