a=int(input())
temp = a
cnt = 0 
while True:
   temp = (temp//10+temp%10)%10+temp%10*10
   cnt+=1
   #print(temp)
   if temp == a:
        break
print(cnt)