import sys
n = int(input())
hash = sys.stdin.readline()
ans = 0
for i in range(len(hash)-1):
    ans += (ord(hash[i])-96)*pow(31,i)
print(ans%1234567891)