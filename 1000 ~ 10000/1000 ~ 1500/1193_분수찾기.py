import sys
a=int(sys.stdin.readline())
k=0
while True:
    k+=1
    a-=k
    if a<=0:
        a+=k
        k+=1
        break
if k%2==1:
    print(f'{a}/{k-a}')
else:
    print(f'{k-a}/{a}')