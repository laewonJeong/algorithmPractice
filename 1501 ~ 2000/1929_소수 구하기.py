def e(n,m):
    arr=[0]*(m+1)
    for i in range(2,m+1):
        arr[i]=i
    k=int(m**0.5)
    for i in range(2,k+1):
        if arr[i]==0:
            continue
        else:
            for j in range(i+i,m+1,i):
                arr[j]=0
    for i in range(n,m+1):
        if arr[i] !=0:
            print(arr[i])
n,m=map(int,input().split())
e(n,m)
