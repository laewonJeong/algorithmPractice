import sys

s = []
a=int(input())
for i in range(a):
    b= int(sys.stdin.readline())
    if b!=0:
        s.append(b)
        #print(s)
    else:
        s.pop()
        #print(s)
print(sum(s))