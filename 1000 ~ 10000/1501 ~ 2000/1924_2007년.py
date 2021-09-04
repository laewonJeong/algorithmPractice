import sys

yoil = ['MON','TUE','WED','THU','FRI','SAT','SUN']
nal = [31,28,31,30,31,30,31,31,30,31,30,31]
month,day = map(int,sys.stdin.readline().split())
total = 0
if month == 1:
    print(yoil[day%7-1])
else:
    for i in range(month-1):
        total += nal[i]
    print(yoil[(day+total)%7-1])