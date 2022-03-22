while(1):
    num = input()
    if num == '0':
        break
    result = 0
    for i in num:
        if i == '0':
            result += 4
        elif i == '1':
            result += 2
        else:
            result += 3
    print(result+2+len(num)-1)