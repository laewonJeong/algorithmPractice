a=int(input())
if a == 1:
    print(1)
else:
    list = []
    for i in range(1):
        list.append(1)
    for i in range(1,1000000000):
        list.append(6*i + list[i-1])
        if(list[i] >=1000000000):
            break
    for i in range(len(list)):
        if a == list[i]:
            print(i+1)
            break
        else:
            if a<list[i]:
                print(i+1)
                break