import sys

def prime(n):
    if n == 1:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1
cnt = 0
a= int(sys.stdin.readline())
n = sys.stdin.readline().split()
for i in n:
    if prime(int(i))==1:
        cnt+=1
print(cnt)