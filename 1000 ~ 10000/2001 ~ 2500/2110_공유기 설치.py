import sys

a,b = map(int,sys.stdin.readline().split())
list = []
for i in range(a):
    x = int(sys.stdin.readline())
    list.append(x)
list = sorted(list)
left = 1
right = list[-1]-list[0]
#print(left,right)
ans = 0
list1=[]
while left<=right:
    if a==b:
        for i in range(1,len(list)):
            list1.append(list[i]-list[i-1])
        list1 = sorted(list1)
        ans = list1[0]
        break
    mid = (left+right)//2
    cnt = 1
    check = list[0]
    for i in range(1,len(list)):
        if list[i] >= check + mid:
            cnt+=1
            check = list[i]
    if cnt>=b:
        left = mid+1
        ans = mid
    else:
        right = mid-1


print(ans)