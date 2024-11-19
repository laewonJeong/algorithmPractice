result = ''
minn = 0
while(1):
    list = []
    list.append(input().split())
    words = []                             
    for i in list[0]:                       
        temp = ''                            
        for j in i:                      
            if j.isalpha() or j == '-':     
                temp += j.lower()
        words.append(temp)
    for i in words:
        if len(i) > minn:
            minn = len(i)
            result = i
    if len(list[0]) != 0:
        if list[0][-1] == 'E-N-D':
            break
print(result)    