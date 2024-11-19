import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
arr = list(map(int,arr))
check = sys.stdin.readline().split()
check = list(map(int,check))
ans=[]
ans1=arr[0]
minimum = 10**9
maximum =-10**9
def dfs(a,arr,result,plus,minus,muli,div):
    if a == len(arr):
        global minimum, maximum
        maximum = max(result, maximum)
        minimum = min(result, minimum)
        return
    if plus >0:
        dfs(a+1,arr,result+arr[a],plus-1,minus,muli,div)
    if minus >0:
        dfs(a+1,arr,result-arr[a],plus,minus-1,muli,div)
    if muli >0:
        dfs(a+1,arr,result*arr[a],plus,minus,muli-1,div)
    if div >0:
        dfs(a+1,arr,int(result/arr[a]),plus,minus,muli,div-1)
dfs(1,arr,arr[0],check[0],check[1],check[2],check[3])
print(maximum)
print(minimum)