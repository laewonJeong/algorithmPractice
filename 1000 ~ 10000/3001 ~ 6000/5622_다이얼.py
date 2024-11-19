a=input()
ans = 0
for i in a:
    if ord(i) < 68:
        ans += 3
    elif ord(i) < 71:
        ans += 4
    elif ord(i) < 74:
        ans += 5
    elif ord(i) < 77:
        ans += 6
    elif ord(i) < 80:
        ans += 7
    elif ord(i) < 84:
        ans += 8
    elif ord(i) < 87:
        ans += 9
    elif ord(i) < 91:
        ans += 10
print(ans)