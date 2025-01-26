import sys
max1 = 0
temp = 0
x,y,z = map(int,sys.stdin.readline().split())
if x == y and y == z:
    temp = 10000 + x*1000
    if max1<temp:
        max1 = temp
elif (x==y and y!=z) or (x==z and x!=y):
    temp = 1000 + x*100
    if max1<temp:
        max1 =temp
elif (y==z and z!=x):
    temp = 1000+ y*100
    if max1<temp:
        max1 = temp
else:
    temp = max(x,y,z)*100
    if max1<temp:
        max1 = temp
print(max1)