import sys
list = [0] *10001
a=int(sys.stdin.readline())
for i in range(a):
    list[int(sys.stdin.readline().rstrip())] += 1
for i in range(10001):
    if list[i] != 0:
        for j in range(list[i]):
            print(i)