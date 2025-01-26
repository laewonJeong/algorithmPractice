import sys

a = sys.stdin.readline()
cnt = 0
for i in range(len(a)-1):
    if (a[i] == 'c' and a[i+1] == '=') or (a[i] == 'c' and a[i+1] == '-'):
        continue
    elif a[i] == 'd' and a[i+1] == '-':
        continue
    elif a[i] == 'd' and a[i+1] == 'z' and a[i+2] == '=':
        continue
    elif a[i] == 'l' and a[i+1] == 'j':
        continue
    elif a[i] == 'n' and a[i+1] == 'j':
        continue
    elif a[i] == 's' and a[i+1] == '=':
        continue
    elif a[i] == 'z' and a[i+1] == '=':
        continue
    elif a[i-1]=='d' and a[i] == 'z' and a[i+1] == '=':
        continue
    else:
        cnt+=1
print(cnt)