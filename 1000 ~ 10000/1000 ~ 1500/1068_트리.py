import sys

check_d={}
def dfs(i):
    global cnt
    check = False
    check_d[i] = 1
    for j in range(len(tree[i])):
        y = tree[i][j]
        if y not in check_d and y in tree[i]:
            check = True
            dfs(y)
    if not check:
        cnt+=1
node = int(sys.stdin.readline())
tree =[[] for i in range(node)]
root =0
cnt = 0
x = sys.stdin.readline().split()
cut = int(sys.stdin.readline())
for i in range(node):
    if x[i] == '-1':
        root = i
        continue
    if int(x[i]) == cut:
        continue
    if i == cut:
        continue
    tree[int(x[i])].append(i)
if cut == root:
    print(0)
else:
    dfs(root)
    print(cnt)