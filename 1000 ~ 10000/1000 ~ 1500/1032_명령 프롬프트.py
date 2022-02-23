n = int(input())
arr = []
result =[]
for i in range(n):
    arr.append(input())
for i in range(n-1):
    for j in range(len(arr[i])):
        if(i==0):
            if arr[i][j] == arr[i+1][j]:
                result.append(arr[i][j])
            else:
                result.append("?")
        else:
            if arr[i+1][j] != result[j]:
                result[j] = "?"
                
for i in result:
    print(i,end="")
if n == 1:
    print(arr[0])