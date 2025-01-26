import sys
def prime(n):
    if n == 1:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1
cnt = 0
m= int(sys.stdin.readline())
n= int(sys.stdin.readline())
list = []
check = 0
for i in range(m,n+1):
    if prime(i) == 1:
        list.append(i)
        check = 1
if check == 0:
    print(-1)
else:
    print(sum(list))
    print(list[0])