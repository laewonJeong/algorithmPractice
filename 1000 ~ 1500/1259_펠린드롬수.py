import sys
while True:
    n = sys.stdin.readline()
    if int(n) == 0:
        break
    if len(n)-1 == 1:
        print('yes')
    elif (len(n) - 1)==2:
        if n[0] == n[1]:
            print('yes')
        else:
            print('no')
    elif (len(n) - 1)==3:
        if n[0] == n[2]:
            print('yes')
        else:
            print('no')
    elif (len(n) - 1)==4:
        if n[0] == n[3] and n[1]==n[2]:
            print('yes')
        else:
            print('no')
    elif (len(n) - 1)==5:
        if n[0] == n[4] and n[1]==n[3]:
            print('yes')
        else:
            print('no')