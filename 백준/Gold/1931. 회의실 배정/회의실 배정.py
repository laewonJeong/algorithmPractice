import sys

n = int(sys.stdin.readline())
arr=[]
for _ in range(n):
    time = list(map(int,sys.stdin.readline().split()))
    arr.append(time)
s_arr = sorted(arr, key=lambda x:(x[1],x[0]))
max = 0
cnt = 1
check = s_arr[0][1]
for i in range(1,len(s_arr)):
    if check <= s_arr[i][0]:
        cnt+=1
        check = s_arr[i][1]
print(cnt)