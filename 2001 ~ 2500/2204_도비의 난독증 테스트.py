import sys
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    list1 = []
    list2 = []
    for _ in range(n):
        a=sys.stdin.readline()
        list2.append(a)
        a=a.upper()
        list1.append(a)
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i] < list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
                temp = list2[i]
                list2[i] = list2[j]
                list2[j] = temp
    print(list2[0],end='')
    list1.clear()
