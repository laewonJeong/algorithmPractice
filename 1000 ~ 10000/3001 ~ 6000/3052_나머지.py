list = []
for i in range(42):
	list.append(0)
for i in range(10):
	a=int(input())
	list[a%42] += 1
cnt=0
for i in list:
	if i!=0:
		cnt+=1
print(cnt)