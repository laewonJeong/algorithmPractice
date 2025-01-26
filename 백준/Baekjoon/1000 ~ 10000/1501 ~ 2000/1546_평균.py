a=int(input())
list = input().split()
max = 0
total = 0
for i in list:
    if int(i)>max:
        max = int(i)
for i in list:
    total += int(i)/max*100
print(total/a)