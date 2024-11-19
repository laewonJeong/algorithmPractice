import math
music,avg = map(int,input().split())
for i in range(music*avg,0,-1):
    if(math.ceil(i/music) < avg):
        ans = i
        break
print(i+1)