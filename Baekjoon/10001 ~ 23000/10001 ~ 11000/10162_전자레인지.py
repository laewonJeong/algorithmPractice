t = int(input())
five_min = 0
one_min = 0
ten_sec = 0

while(True):
    if t >= 300:
        t-=300
        five_min +=1
    elif t>=60:
        t-=60
        one_min+=1
    else:
        t-=10
        ten_sec+=1
    if t == 0 or t < 10:
        break
if t == 0:
    print(f"{five_min} {one_min} {ten_sec}")
else:
    print(-1)