import sys
arr=[]
for i in range(1,31):
    arr.append(i)
for _ in range(28):
    x=int(input())
    arr.remove(x)
arr=sorted(arr)
print(arr[0])
print(arr[1])