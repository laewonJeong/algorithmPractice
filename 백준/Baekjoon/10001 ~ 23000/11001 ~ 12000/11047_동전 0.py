import sys

n,k = map(int,sys.stdin.readline().split())
money = []
cnt = 0
for _ in range(n):
    money.append(int(sys.stdin.readline()))
money = sorted(money,key = lambda x:-x)
for i in money:
    if k>=i:
        cnt += k//i
        k-=i*(k//i)
print(cnt)