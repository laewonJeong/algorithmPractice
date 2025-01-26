a=input()
list = []
for i in range(26):
	list.append(-1)
for i in range(len(a)):
	if list[ord(a[i])-97] == -1:
		list[ord(a[i])-97] = i
for i in list:
	print(i,end=' ')