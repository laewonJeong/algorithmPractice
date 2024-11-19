a,b = map(int,input().split())
arr = input().split()
ans = []
for i in arr:
    c = int(i)-a*b
    ans.append(c)
for i in ans:
    print(i,end=' ')