n,m = map(int,input().split())
arr=[[] for i in range(n)]

for i in range(n):
    temp = input().split()
    for j in temp:
        arr[i].append(int(j))
k = int(input())
for _ in range(k):
    i,j,x,y = map(int, input().split())
    result = 0
    for a in range (i-1,x):
        for b in range (j-1,y):
            result += arr[a][b]
    print(result)