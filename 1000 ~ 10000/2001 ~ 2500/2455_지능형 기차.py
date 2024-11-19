import sys
maximum=-1
people_num = 0
for _ in range(4):
    n,m = map(int,sys.stdin.readline().split())
    people_num -= n
    people_num += m
    if people_num > maximum:
        maximum = people_num
print(maximum)
