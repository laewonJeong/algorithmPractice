import sys

def cut(x,y,n):
    one = True
    zero = True
    for i in range(y,y+n):
        for j in range(x,x+n):
            if paper[i][j] == '0':
                one = False
            if paper[i][j] == '1':
                zero = False
    if zero == True:
        wPaper.append(1)
    elif one == True:
        bPaper.append(1)
    else:
        cut(x,y,n//2)
        cut(x+n//2,y,n//2)
        cut(x,y+n//2,n//2)
        cut(x+n//2,y+n//2,n//2)
    return wPaper,bPaper

n = int(sys.stdin.readline())
paper = []
wPaper=[]
bPaper=[]
for i in range(n):
    paper.append(sys.stdin.readline().split())
a,b=cut(0,0,n)
print(sum(a))
print(sum(b))