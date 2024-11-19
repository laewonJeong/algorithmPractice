a,b = map(int,input().split())
arr = input().split()
list = []
for i in arr:
	if int(i) < b:
		list.append(i)
for i in list:
	print(i,end=' ')