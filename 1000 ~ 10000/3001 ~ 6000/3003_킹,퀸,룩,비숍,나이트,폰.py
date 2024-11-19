import sys
check = [1,1,2,2,2,8]
list = sys.stdin.readline().split()
ans = []
for i in range(len(list)):
    if int(list[i])!=check[i]:
        ans.append((check[i]-int(list[i])))
    else:
        ans.append(0)
for i in ans:
    print(i,end=' ')