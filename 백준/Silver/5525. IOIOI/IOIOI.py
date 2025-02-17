import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

i = 0
answer = 0
count = 0

while i <= m-2:
    if s[i:i+3] == 'IOI':
        count += 1
        i += 2
        if count == n:
            answer += 1
            count -= 1
    else:
        count = 0
        i+=1
        
print(answer)