import sys
n = sys.stdin.readline()
s=[]
cnt = 0
check = 0
for i in range(len(n)):
    if i==len(n)-1 and len(s) == 2:
        a = int(s[0])*10+int(s[1])
        s.clear()
        cnt+=1
        break
    elif i==len(n)-1 and len(s) == 1:
        a = int(s[0])
        s.clear()
        cnt+=1
        break
    if n[i] == '/':
        if cnt == 0 and len(s) == 2:
            k = int(s[0])*10+int(s[1])
            s.clear()
            cnt+=1
        elif cnt == 0 and len(s) == 1:
            k = int(s[0])
            s.clear()
            cnt+=1
        elif cnt == 1 and len(s) == 2:
            d = int(s[0])*10+int(s[1])
            s.clear()
            cnt+=1
        elif cnt==1 and len(s) == 1:
            d = int(s[0])
            s.clear()
            cnt+=1
    else:
        s.append(n[i])
if k+a<d or d==0:
    print('hasu')
else:
    print('gosu')