str = input()
str = str.upper()
list = []
for i in range(26):
    list.append(0)
for i in str:
    list[int(ord(i))-65]+=1
max = 0
for i in range(26):
    if list[i]>max:
        max = list[i]
        ans = i
cnt = 0
for i in list:
    if max == i:
        cnt+=1
if cnt > 1:
    print('?')
else:
    print(chr(ans+65))