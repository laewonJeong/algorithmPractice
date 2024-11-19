nan =[]
result = 0
check = 0
for i in range(9):
    nan.append(int(input()))
    result += nan[i]
for i in range(len(nan)):
    for j in range(len(nan)):
        if result-(nan[i]+nan[j]) == 100 and i!=j:
            a= nan[i]
            b= nan[j]
            nan.remove(a)
            nan.remove(b)
            check = 1
            break
    if check ==1:
        break
nan.sort()
for i in nan:
    print(i)

