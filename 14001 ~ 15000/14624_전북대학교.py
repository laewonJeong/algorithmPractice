import sys
n=int(sys.stdin.readline())
if n%2 ==0:
    print('I LOVE CBNU')
else:
    for i in range(n//2+2):
        for j in range(n):
            if i ==0:
                print('*',end='')
            elif i ==1 and j==n//2:
                print('*',end='')
                break
            elif i>1:
                if j == n//2+1-i:
                    print('*',end='')
                elif j==(n//2+1-i)+(i*2-1)-1:
                    print('*',end='')
                    break
                else:
                    print(' ', end='')
            else:
                print(' ',end='')

        print("")