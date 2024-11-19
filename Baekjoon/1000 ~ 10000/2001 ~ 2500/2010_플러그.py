import sys
temp = 0
n = int(sys.stdin.readline())
for _ in range(n):
    x=int(sys.stdin.readline())
    temp+=x
print(temp-(n-1))