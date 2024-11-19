import sys

channel = int(sys.stdin.readline())
n = int(sys.stdin.readline())
temp = sys.stdin.readline().split()
button=[]
check=[0]*10
for i in temp:
    button.append(int(i))
    check[int(i)] = 1
button.clear()
for i in range(10):
    if check[i] == 0:
        button.append(i)
min_cnt = abs(100-channel)
for i in range(1000000):
    for j in range(len(str(i))):
        if int(str(i)[j]) not in button:
            break
        elif len(str(i))-1 == j:
            min_cnt = min(min_cnt,len(str(i))+abs(i-channel))
print(min_cnt)