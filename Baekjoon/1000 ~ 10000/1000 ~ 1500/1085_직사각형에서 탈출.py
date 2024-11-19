import sys
x,y,w,h = map(int,sys.stdin.readline().split())
min1 = min(h-y,w-x)
min2 = min(y,x)
print(min(min1,min2))