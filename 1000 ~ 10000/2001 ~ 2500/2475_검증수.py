a=input().split()
ans = 0
for i in a:
    ans += int(i)*int(i)
print(ans%10)