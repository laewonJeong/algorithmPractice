import sys
a,b,c,d=map(int,sys.stdin.readline().split())
e,f,g,h=map(int,sys.stdin.readline().split())

if a+b+c+d > e+f+g+h:
    print(a+b+d+c)
elif a+b+c+d < e+f+g+h:
    print(e+f+g+h)
else:
    print(a+b+d+c)