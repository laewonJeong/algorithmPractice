import sys

a = sys.stdin.readline()
ans = 0
for i in range(1,1000001):
    for j in str(i):
        ans+=int(j)
    #print(i+ans)
    if(i>int(a)):
        break
    if i + ans == int(a):
        check = 1
        ans = i
        break
    else:
        check = 0
        ans = 0
if check == 0:
    print(0)
else:
    print(ans)