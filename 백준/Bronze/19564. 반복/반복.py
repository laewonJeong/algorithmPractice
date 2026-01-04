import sys

word = sys.stdin.readline().strip()
ans = 1

for i in range(1, len(word)):
    if word[i] <= word[i-1]:
        ans += 1

print(ans)