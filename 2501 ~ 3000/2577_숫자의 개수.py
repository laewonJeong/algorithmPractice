a=input()
b=input()
c=input()
ans = int(a)*int(b)*int(c)
ans1 = str(ans)
list = []
for i in range(10):
	list.append(0)
for i in ans1:
	list[int(i)] += 1
for i in range(10):
	print(list[i])