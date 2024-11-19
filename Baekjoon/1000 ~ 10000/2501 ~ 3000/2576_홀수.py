temp =[]
holsu = []
for _ in range(7):
    temp.append(int(input()))
for i in temp:
    if i%2 != 0:
        holsu.append(i)
if len(holsu) == 0:
    print(-1)
else:
    print(sum(holsu))
    print(min(holsu))