import sys
n=int(sys.stdin.readline())
temp = []
for _ in range(n):
    x,y = sys.stdin.readline().split()
    for i in range(len(y)):
        if i == int(x)-1:
            continue
        temp.append(y[i])
    for i in temp:
        print(i,end='')
    temp.clear()
    print('')
