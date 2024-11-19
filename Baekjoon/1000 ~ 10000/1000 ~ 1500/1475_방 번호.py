room_num = input()
arr = [0 for i in range(10)]
result = 0
for i in room_num:
    if int(i) == 9 and arr[9] > arr[6]:
        arr[6]+=1
    elif int(i) == 6 and arr[6] > arr[9]:
        arr[9]+=1
    else:
        arr[int(i)]+=1
print(max(arr))