import sys

input = sys.stdin.readline

n, m = map(int, input().split())

know = set(list(map(int, input().split()))[1:])

parties = []
for _ in range(m):
    parties.append(list(map(int, input().split()))[1:])

while True:
    updated = False

    for party in parties:
        if all(person not in know for person in party):
            continue
        for person in party:
            if person not in know:
                know.add(person)
                updated = True

    if not updated:
        break                

answer = 0
for party in parties:
    if all(person not in know for person in party):
        answer += 1

print(answer)