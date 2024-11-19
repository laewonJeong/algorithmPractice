import sys

def binary_search(arr,k,left,right):
    if left > right:
        return 0
    mid =(left+right)//2
    if arr[mid] == k:
        return 1
    elif arr[mid]>k:
        return binary_search(arr,k,left,mid-1)
    else:
        return binary_search(arr,k,mid+1,right)
n=int(sys.stdin.readline())
check = sys.stdin.readline().split()
check = list(map(int,check))
n1=int(sys.stdin.readline())
list1 = sys.stdin.readline().split()
list1 = list(map(int,list1))
check = sorted(check)
for i in list1:
    print(binary_search(check,i,0,len(check)-1))