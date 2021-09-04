import sys
import math
n=int(sys.stdin.readline())
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    if b-a <=3:
        print(b-a)
    else:
        n = int(math.sqrt(b-a))
        if pow(n,2) == b-a:
            print(2*n-1)
        elif pow(n,2) < b-a<=pow(n,2)+n:
            print(2*n)
        else:
            print(2*n+1)