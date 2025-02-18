class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        answer = []

        def backtracking(pattern, now, now_len, visited, idx):
            nonlocal answer
            if answer or now_len == n+1 or idx == len(pattern):
                if now_len == n+1:
                    answer = ''.join(list(map(str, now)))
                return

            p = pattern[idx]

            for i in range(1, n+2):
                if not visited[i]:
                    if p == 'I' and now[-1] < i:
                        visited[i] = True
                        now.append(i)

                        backtracking(pattern, now, now_len + 1, visited, idx+1)

                        visited[i] = False
                        now.pop()
                    elif p == 'D' and now[-1] > i:
                        visited[i] = True
                        now.append(i)

                        backtracking(pattern, now, now_len + 1, visited, idx+1)

                        visited[i] = False
                        now.pop()

        for i in range(1, n+2):
            visited = [False] * (n+2)
            visited[i] = True
            backtracking(pattern, [i], 1, visited, 0)

            if answer:
                return answer