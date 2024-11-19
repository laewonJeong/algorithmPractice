import sys
n=int(sys.stdin.readline())
s = []
stack = []
ans = []
for i in range(n):
    s.append(int(sys.stdin.readline()))
cnt = 0
check = 1
for i in s:
    while cnt<i:
        cnt +=1
        stack.append(cnt)
        ans.append('+')
    if stack[-1] == i:
        stack.pop()
        ans.append('-')
    else:
        check = 0
if check == 0:
    print('NO')
else:
    for i in ans:
        print(i)