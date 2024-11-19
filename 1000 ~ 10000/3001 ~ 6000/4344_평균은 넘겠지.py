a=int(input())
temp = 0
for i in range(a):
    list = input().split()
    for i in range(1,len(list)):
        temp += int(list[i])
    #print(temp)
    avg = temp/int(list[0])
    #print(avg)
    cnt = 0
    for i in range(1,len(list)):
        if int(list[i]) > avg:
            cnt += 1
    print(format(cnt/int(list[0])*100,".3f")+'%')
    cnt = 0
    temp = 0