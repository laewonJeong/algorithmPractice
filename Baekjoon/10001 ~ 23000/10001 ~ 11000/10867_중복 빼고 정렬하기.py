n = int(input())
arr = input().split()
result = map(int,arr)
result = list(result)
result = set(result)
result = list(result)
result.sort()
for i in result:
    print(i, end=" ")