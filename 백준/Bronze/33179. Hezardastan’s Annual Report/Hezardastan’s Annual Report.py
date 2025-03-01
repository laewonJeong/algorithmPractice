n=int(input())
print(sum([x//2 if x%2==0 else x//2+1 for x in list(map(int,input().split()))]))