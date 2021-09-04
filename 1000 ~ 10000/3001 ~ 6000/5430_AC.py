from collections import deque
import sys

n = int(sys.stdin.readline())
while n!=0:
    d=deque()
    check = 0
    cmd = sys.stdin.readline()
    length = int(sys.stdin.readline())
    if(length == 0):
        input_arr = sys.stdin.readline()
        input_arr = []
    else:
        input_arr = list(map(int,input()[1:-1].split(',')))
    for i in input_arr:
        d.append(i)
    checking = 1
    for i in cmd:
        if i == 'R':
            if checking == 1:
                checking = 0
            elif checking == 0:
                checking = 1
        elif i == 'D':
            if(len(d) != 0):
                if checking == 1:
                    d.popleft()
                else:
                    d.pop()
            else:
                print('error')
                check = 1
                break
    if cmd.count('R') %2 !=0:
        d.reverse()
    if check != 1:
        if len(d) == 1:
            print(f'[{d[0]}]')
        elif len(d) == 0:
            print('[]')
        else:
            for i in range(len(d)):
                if i == 0:
                    print(f'[{d[i]},',end='')
                elif i == len(d)-1:
                    print(f'{d[i]}]')
                else:
                    print(f'{d[i]},',end='')
        check = 0
    d.clear()
    n-=1