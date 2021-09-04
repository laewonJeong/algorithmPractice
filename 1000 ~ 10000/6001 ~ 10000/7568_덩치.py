import sys

n = int(sys.stdin.readline())
list_a = [[0]*2]*n
ans=[]
for i in range(n):
    list_a[i] = list(map(int,sys.stdin.readline().split()))
for i in range(n):
    big = 1
    for j in range(n):
        if i == j:
            continue
        elif list_a[i][0] < list_a[j][0] and list_a[i][1]<list_a[j][1]:
            big += 1
    ans.append(big)
for i in ans:
    print(i,end=' ')