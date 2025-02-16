from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        answer = [0] * ((n - 1) * 2 + 1)
        visited = [False] * (n + 1)
        result = None

        def dfs(idx):
            nonlocal result
            if result:
                return

            if idx == (n - 1) * 2 + 1:
                result = answer[:]
                return
            
            if answer[idx] != 0:
                dfs(idx + 1)
                return

            for i in range(n, 0, -1):
                if visited[i]:
                    continue
                
                if i == 1:
                    answer[idx] = i
                    visited[i] = True
                    dfs(idx + 1)
                    visited[i] = False
                    answer[idx] = 0
                else:
                    if idx + i >= (n - 1) * 2 + 1 or answer[idx + i] != 0:
                        continue

                    answer[idx] = i
                    answer[idx + i] = i
                    visited[i] = True

                    dfs(idx + 1)

                    visited[i] = False
                    answer[idx] = 0
                    answer[idx + i] = 0

        dfs(0)
        return result
