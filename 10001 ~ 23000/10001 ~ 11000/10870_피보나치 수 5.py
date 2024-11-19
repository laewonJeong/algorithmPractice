import sys
def fib(a):
    if a == 0:
        return 0
    elif a==1:
        return 1
    elif a==2:
        return 1
    else:
        return fib(a-1)+fib(a-2)
a=int(input())
print(fib(a))