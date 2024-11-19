def check():
    list = []
    for i in range(1,10001):
        for j in range(len(str(i))):
            if len(str(i))==1:
                list.append(i+i)
            elif len(str(i))==2:
                list.append(i+int(str(i)[0])+int(str(i)[1]))
            elif len(str(i))==3:
                list.append(i+int(str(i)[0])+int(str(i)[1])+int(str(i)[2]))
            elif len(str(i))==4:
                list.append(i+int(str(i)[0])+int(str(i)[1])+int(str(i)[2])+int(str(i)[3]))
    for i in range(1,10001):
        if i in list:
            b=1
        else:
            print(i)

check()