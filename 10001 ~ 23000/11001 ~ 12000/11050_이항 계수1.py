import sys
n,k = map(int,sys.stdin.readline().split())
def factorial(n):
    temp = 1
    for i in range(1,n+1):
        temp = temp*i
    return temp
print(factorial(n)//(factorial(k)*factorial(n-k)))
