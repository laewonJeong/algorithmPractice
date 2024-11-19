import sys
a,max_num=map(int,sys.stdin.readline().split())
card = sys.stdin.readline().split()
max = 0
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if int(card[i])+int(card[j])+int(card[k]) <= max_num and max<int(card[i])+int(card[j])+int(card[k]):
                max = int(card[i])+int(card[j])+int(card[k])
print(max)