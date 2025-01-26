a=int(input())
count=0
ans=0
for i in range(a):
    OX = input()
    for j in OX:
        if j == 'O':
            count += 1
            ans += count
        else:
            count = 0
    print(ans)
    count = 0
    ans = 0