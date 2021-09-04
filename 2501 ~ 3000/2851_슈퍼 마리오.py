import sys
arr=[0]*10
for i in range(10):
    n = int(sys.stdin.readline())
    if i == 0:
        arr[i] = n
    else:
        arr[i] = arr[i-1]+n
for i in range(10):
    if arr[i] == 100:
        print(100)
        break
    if arr[i] > 100:
        if 100 - arr[i-1] < arr[i] - 100:
            print(arr[i-1])
            break
        elif 100 - arr[i-1] > arr[i] - 100:
            print(arr[i])
            break
        elif 100 - arr[i-1] == arr[i] - 100:
            print(arr[i])
            break
    if i == 9:
        print(arr[i])
        break

