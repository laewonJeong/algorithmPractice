import sys
from collections import deque

input = sys.stdin.readline

g_string = [deque() for _ in range(6)]

n, p = map(int, input().split())

for _ in range(n):
    s_num, p_num = map(int, input().split())
    g_string[s_num-1].append(p_num)

answer = 0
for i in range(6):
    stack = []
    while g_string[i]:
        if not stack:
            stack.append(g_string[i].popleft())
            answer += 1

        elif stack[-1] < g_string[i][0]:
            stack.append(g_string[i].popleft())
            answer += 1

        elif stack[-1] > g_string[i][0]:
            while stack:
                answer += 1
                if stack[-1] == g_string[i][0]:
                    g_string[i].popleft()
                    answer -= 1
                    break
                elif stack[-1] < g_string[i][0]:
                    stack.append(g_string[i].popleft())
                    break
                else:
                    stack.pop()

        elif stack and stack[-1] == g_string[i][0]:
            g_string[i].popleft()

print(answer)