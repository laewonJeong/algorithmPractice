a=input()
b=input().split()
cnt = 0
for i in b:
    if int(i) == int(a):
        cnt+=1
print(cnt)