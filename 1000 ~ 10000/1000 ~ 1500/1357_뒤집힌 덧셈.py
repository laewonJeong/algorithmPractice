import sys
def rev(n):
    if len(n) == 1:
        return int(n)
    elif len(n) == 2:
        return (int(n)%10*10) + int(n)//10
    elif len(n) == 3:
        return (int(n)%10*100) + (int(n)//100) + ((int(n)//10%10)*10)
    else:
        return 1
n,m = sys.stdin.readline().split()
ans = rev(n)+rev(m)
a = str(ans)
a=list(a)
a.reverse()
check = 0
for i in range(len(a)):
    if a[i] == '0' and check == 0:
        continue
    if a[i] != 0:
        check =1
    print(f'{a[i]}',end='')