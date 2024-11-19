import sys
from collections import Counter
def binary_search(arr,k,left,right):
    if left > right:
        return 0
    while left<=right:
        mid =(left+right)//2
        if arr[mid] == k:
            return 1
        elif arr[mid]>k:
            right = mid-1
        else:
            left = mid+1
    return 0
n=int(sys.stdin.readline())
check = sys.stdin.readline().split()
check = list(map(int,check))
n1=int(sys.stdin.readline())
list1 = sys.stdin.readline().split()
list1 = list(map(int,list1))
check = sorted(check)
ans = Counter(check)
#print(ans)
ret =[0]*n1
for i in range(n1):
    idx = binary_search(check,list1[i],0,len(check)-1)
    if idx == 0:
        continue
    ret[i] = ans[list1[i]]
for i in ret:
    print(i,end=' ')