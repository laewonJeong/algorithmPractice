import sys

input = sys.stdin.readline


n = int(input().strip())
a = list(map(int, input().split()))

m = int(input().strip())
b = list(map(int, input().split()))

common = set(a) & set(b)
if not common:
    print(0)
else:
    answer_len = 0
    answer = ""
    while common:
        max_num = max(common)
        answer += str(max_num) + " "
        answer_len += 1

        a = a[a.index(max_num)+1:]
        b = b[b.index(max_num)+1:]

        common = set(a) & set(b)
    
    print(answer_len)
    print(answer)