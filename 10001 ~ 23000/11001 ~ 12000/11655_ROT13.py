import sys
pwd = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
PWD = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
x = input()
ans = []
for i in x:
    if ord(i) >=65 and ord(i)<97:
        ans.append(PWD[ord(i)-65])
    elif ord(i) >=97:
        ans.append(pwd[ord(i)-97])
    else:
        ans.append(i)
for i in ans:
    print(i,end='')
