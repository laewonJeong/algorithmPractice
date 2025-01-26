import sys
n,m = map(int,sys.stdin.readline().split())
W,L,Bronze = map(int,sys.stdin.readline().split())
dic={}
ans=[]
score = 0
check = 0
for i in range(m):
    a,b = sys.stdin.readline().split()
    dic[a] =b
for i in range(n):
    a=sys.stdin.readline().rstrip()
    if a not in dic:
        ans.append('L')
    else:
        ans.append(dic[a])
for i in ans:
    if i == 'W':
        score += W
    else:
        score -= L
        if score <0:
            score = 0
    if score >= Bronze:
        check = 1
if check == 1:
    print('I AM NOT IRONMAN!!')
else:
    print('I AM IRONMAN!!')