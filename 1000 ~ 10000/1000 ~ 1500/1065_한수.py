import sys
def checking(a):
    cnt = 0
    for i in range(1,int(a)+1):
        if(i<100):
           cnt+=1
        else:
            if i%100//10-i//100 == i%10 - i%100//10:
                cnt+=1
    return cnt
a = sys.stdin.readline()
print(checking(a))