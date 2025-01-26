import sys
from collections import defaultdict

n = sys.stdin.readline()
my_card = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
answer = list(map(int, sys.stdin.readline().split()))

dic = defaultdict(bool)
for card in my_card:
    dic[card] = True

for i in range(m-1):
    if dic[answer[i]]:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
print(int(dic[answer[-1]]))