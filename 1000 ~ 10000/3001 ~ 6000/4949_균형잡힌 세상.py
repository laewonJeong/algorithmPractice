import sys

def check(n):
    for i in n:
        if i=='(' or i=='[':
            s.append(i)
        elif len(s)==0 and (i ==')' or i ==']'):
            return 0
        elif (len(s) != 0 and s[len(s)-1] == '(') and i == ')':
            s.pop()
        elif (len(s) != 0 and s[len(s)-1] == '[') and i ==']':
            s.pop()
        elif (len(s) != 0 and s[len(s)-1] == '(') and i ==']':
            return 0
        elif (len(s) != 0 and s[len(s)-1] == '[') and i ==')':
            return 0
    if len(s) == 0:
        return 1
    else:
        return 0
s = []
while True:
    b = sys.stdin.readline().rstrip()
    if b[0] == '.':
        break
    if check(b) == 1:
        print('yes')
    else:
        print('no')
    while len(s)!=0:
        s.pop()