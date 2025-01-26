n,k = map(int, input().split())
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])
arr.sort()
print(arr[k-1])