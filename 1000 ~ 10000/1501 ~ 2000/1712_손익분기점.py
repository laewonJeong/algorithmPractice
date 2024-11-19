a,b,c = map(int,input().split())
if b>=c:
    print(-1)
else:
    profit = c-b
    x = a//profit
    print(x+1)