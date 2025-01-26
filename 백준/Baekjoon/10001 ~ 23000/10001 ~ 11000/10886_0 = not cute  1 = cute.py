import sys
n=int(sys.stdin.readline())
cnt1=0
cnt0=0
for _ in range(n):
    x=int(sys.stdin.readline())
    if x == 0:
        cnt0+=1
    else:
        cnt1+=1
if cnt0>cnt1:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')