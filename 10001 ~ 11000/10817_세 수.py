import sys

a,b,c = map(int,sys.stdin.readline().split())
list = []
list.append(a)
list.append(b)
list.append(c)
list = sorted(list)
print(list[1])