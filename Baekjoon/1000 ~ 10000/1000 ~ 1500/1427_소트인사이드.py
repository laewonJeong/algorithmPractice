import sys
a=sys.stdin.readline()
a=sorted(a)
a.reverse()
for i in a:
    if a!='\n':
        print(i,end='')
