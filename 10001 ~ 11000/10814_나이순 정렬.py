import sys
a=int(sys.stdin.readline())
list1 = [[0 for col in range(3)] for row in range(a)]
for i in range(a):
    b,c = sys.stdin.readline().split()
    list1[i][0] = b
    list1[i][1] = c
    list1[i][2] = i+1
list1.sort(key = lambda x:[int(x[0]),int(x[2])])
for i in range(a):
    print(f'{list1[i][0]} {list1[i][1]}')