hour,min = map(int,input().split())
for i in range(45):
	min-=1
	if min == -1:
		min = 59
		hour -=1
		if hour == -1:
			hour = 23
print(hour,min)