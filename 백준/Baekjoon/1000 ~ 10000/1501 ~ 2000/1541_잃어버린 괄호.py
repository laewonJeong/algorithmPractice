import sys

n = sys.stdin.readline()
list = []
list1=[]
temp=''
for i in n:
    if ord(i)>=48 and ord(i)<=57 or i == '+':
        temp+=i
        continue
    list.append(temp)
    temp = ''
for i in list:
    temp = 0
    cnt = i.split('+')
    for j in cnt:
        temp += int(j)
    list1.append(temp)
result = list1[0]
for i in range(1,len(list1)):
    result-=list1[i]
print(result)