import sys
dic = {}
name = []
ans = []
n=int(sys.stdin.readline())
for i in range(n):
    a,b = sys.stdin.readline().split()
    dic[a] =b
    name.append(a)
my_set = set(name)
name = list(my_set)
for i in name:
    if dic[i] == 'enter':
        ans.append(i)
ans = sorted(ans,reverse=True)
for i in ans:
    print(i)