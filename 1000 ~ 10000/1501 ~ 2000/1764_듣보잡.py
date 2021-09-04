import sys
n,m=map(int,sys.stdin.readline().split())
list1=[]
for _ in range(n+m):
    list1.append(sys.stdin.readline().rstrip())
list1 = sorted(list1)
ans=[]
for i in range(1,n+m):
    if list1[i] == list1[i-1]:
        ans.append(list1[i])
print(len(ans))
for i in ans:
    print(i)