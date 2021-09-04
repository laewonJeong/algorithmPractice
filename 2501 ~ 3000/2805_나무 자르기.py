import sys

def binary_search(arr,k,n,m):
    while n<=m:
        mid = (n+m)//2
        #print('mid = ', mid)
        cnt = 0
        for i in arr:
            temp= i-mid
            if temp <0:
                temp = 0
            cnt += temp
            #print(cnt)
        if cnt >= k:
            n = mid+1
        else:
            m= mid-1
    return m
a,b = map(int,sys.stdin.readline().split())
max = 0
min = 20000000000
list = []
x=sys.stdin.readline().split()
for i in x:
    if int(i)>max:
        max = int(i)
    if int(i)<min:
        min = int(i)
    list.append(int(i))
    #print(min,max)
if min == max:
    print(binary_search(list,b,1,max))
else:
    print(binary_search(list,b,min,max))