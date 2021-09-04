a=int(input())
for j in range(a):
    x,y = input().split()
    for i in y:
        print(i*int(x),end = '')
    print(' ')