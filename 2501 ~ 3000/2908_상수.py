a,b = map(int,input().split())
a = a%10*100+a//100+a%100//10*10
b = b%10*100+b//100+b%100//10*10
print(max(a,b))