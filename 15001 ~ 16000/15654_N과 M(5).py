import sys
check={}
arr1=[]
def dfs(a):
    if a == m:
        print(' '.join(map(str, check)))
        return
    for i in range(len(arr)):
        if arr[i] not in check:
            check[arr[i]] = 1
            arr1.append(arr[i])
            dfs(a+1)
            arr1.pop()
            check.pop(arr[i])
            
n,m = map(int,sys.stdin.readline().split())
arr=[]
a = sys.stdin.readline().split()
for i in a:
    arr.append(int(i))
arr.sort()
dfs(0)