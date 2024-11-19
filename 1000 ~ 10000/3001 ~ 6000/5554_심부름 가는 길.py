import sys
list = []
for i in range(4):
    list.append(int(sys.stdin.readline()))
print(sum(list)//60)
print(sum(list)%60)