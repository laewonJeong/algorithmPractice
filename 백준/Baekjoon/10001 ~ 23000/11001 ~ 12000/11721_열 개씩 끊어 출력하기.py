import sys

a=sys.stdin.readline()
for i in range(len(a)):
    if i == len(a)-1:
        break
    if (i+1)%10 == 0:
        print(f'{a[i]}\n',end='')
    else:
        print(a[i], end='')