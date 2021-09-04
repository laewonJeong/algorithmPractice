import sys
n = sys.stdin.readline().rstrip()
if len(n) == 2:
    print(int(n[0])+int(n[1]))
elif len(n) == 4:
    print(10+10)
else:
    if n[len(n)-1] == '0':
        print(int(n[0])+10)
    else:
        print(10+int(n[-1]))