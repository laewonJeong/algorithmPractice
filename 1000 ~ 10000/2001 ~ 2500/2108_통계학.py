import sys
a=int(sys.stdin.readline())
list=[]
bindo=[]
for i in range(a):
    list.append(int(sys.stdin.readline().rstrip()))
print(round(sum(list)/a))   #평균

list = sorted(list)         
print(list[a//2])           #중앙값

list1 =[0]*8002             #빈도수
for i in list:
    if i<0:
        list1[abs(i)] += 1
    elif i == 0:
        list1[0] += 1
    else:
        list1[i+4000] += 1
max = 0
for i in range(8002):
    if list1[i] > max:
        max = list1[i]
        ans = i
cnt = 0
for i in range(8002):
    if max == list1[i]:
        cnt+=1
if cnt == 1:
    if ans<=4000:
        print(ans*-1)
    else:
        print(ans-4000)
else:
    cnt = 0
    for i in range(8002):
        if max == list1[i]:
            if i==0:
                bindo.append(0)
            elif i<=4000:
                bindo.append(i*-1)
            else:
                bindo.append(i-4000)
    bindo = sorted(bindo)
    print(bindo[1])

print(list[a-1]-list[0]) #최대 - 최소