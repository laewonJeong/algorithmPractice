a=input()
ans = 0
k=len(a)-1
for i in range(len(a)):
    if ord(a[i])>=ord('A'):
        ans+=(int(ord(a[i]))-55)*pow(16,k)
    else:
        ans += int(a[i])*pow(16,k)
    k-=1
print(ans)