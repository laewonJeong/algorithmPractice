n=int(input())
n = "%.300f"%2**-n
temp = 0
for i in range(len(n)-1,1,-1):
    if n[i] != '0':
        temp = i
        break
print(n[:temp+1])