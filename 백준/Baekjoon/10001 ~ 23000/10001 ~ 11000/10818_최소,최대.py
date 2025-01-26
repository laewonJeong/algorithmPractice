a=int(input())
arr = input().split()
min=1000001
max=-1000001
for i in arr:
    if int(i)<min:
        min = int(i)
    if int(i)>max:
        max = int(i)
print(min,max)