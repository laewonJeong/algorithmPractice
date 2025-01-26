import sys

def fac(n):
    ans = 1
    for i in range(1,n+1):
        ans=ans*i
    return ans
n = int(sys.stdin.readline())
str_f = str(fac(n))
cnt = 0
for i in range(len(str_f)-1,-1,-1):
    if str_f[i] == '0':
        cnt+=1
        if str_f[i-1] != '0':
            break
print(cnt)