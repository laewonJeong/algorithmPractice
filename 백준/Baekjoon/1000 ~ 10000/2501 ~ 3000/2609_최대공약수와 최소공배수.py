import sys
def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b,a%b)

n,m = map(int,sys.stdin.readline().split())
if n>m:
    max = n
else:
    max = m
print(GCD(n,m))
print(n*m//GCD(n,m))
