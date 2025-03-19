import sys

input = sys.stdin.readline

n, m = map(int, input().split())

city = []
houses = []
chicken = []

for i in range(n):
    city.append(list(map(int, input().split())))
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

answer = float('inf')
def backtracking(start, now, chosen):
    global answer
    if now == m:
        total = 0
        for house in houses:
            distance = float('inf')
            for c in chosen:
                distance = min(distance, abs(house[0] - chicken[c][0]) + abs(house[1] - chicken[c][1]))
            total += distance

        answer = min(answer, total)
        return

    for i in range(start, len(chicken)):
        if i not in chosen:
            chosen.append(i)
            backtracking(i+1, now + 1, chosen)
            chosen.pop()

backtracking(0, 0, [])

print(answer)