n,k = map(int,input().split())
a = []
for i in range(n):
    a.append(i+1)
answer = []
num = 0
for _ in range(n):
    num += k-1
    if num >= len(a):
        num = num%len(a)

    answer.append(str(a.pop(num)))
for i in range(len(answer)):
    if i == 0:
        print("<",end="")
    if i == len(answer)-1:
        print(answer[i],end="")
        print(">")
    else:
        print(answer[i],end="")
        print(", ",end="")