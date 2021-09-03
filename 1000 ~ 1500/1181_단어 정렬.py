import sys
a=int(sys.stdin.readline())
list1 = []
for i in range(a):
    str = sys.stdin.readline()
    list1.append(str)
list1 = list(set(list1))
list1.sort(key = lambda x:[len(x),x])
for i in range(len(list1)):
        print(list1[i],end='')