import sys

def check(n):
    for i in n:
        if i=='(':
            s.append(i)
            #print(s)
        elif len(s)==0 and i ==')':
            return 0
        elif len(s) != 0 and i ==')':
            s.pop()
            #print(s)
    if len(s) == 0:
        return 1
    else:
        return 0
s = []
a=int(input())
for i in range(a):
    b=sys.stdin.readline()
    if check(b) == 1:
        print('YES')
    else:
        print('NO')
    while len(s) !=0:
        s.pop()