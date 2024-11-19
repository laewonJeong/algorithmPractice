import sys
a=int(sys.stdin.readline())
if a%5==0:
    print(a//5)
elif a<3 or a>5000:
    print(-1)
else:
    x=a
    five = x//5
    cnt = 0
    check = 0
    for i in range(five,-1,-1):
        #print(i)
        x=a
        x=x-5*i
        while True:
            if(x<=0):
                break
            x=x-3
            cnt+=1
        if(x==0):
            print(i+cnt)
            check = 1
            break 
        else:
            cnt = 0
    if check == 0:
        print(-1)