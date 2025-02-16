class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        answer = [0] * ((n - 1) * 2 + 1)
        visited = [False] * (n + 1)

        result = []
        def dfs(idx):
            if result:
                return
            if 0 not in answer:
                result.append(answer[:])
                return
            
            if answer[idx] != 0:
                dfs(idx + 1)

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
                    while idx < len(answer) and answer[idx] != 0:
                        idx += 1

                    if idx + i >= len(answer) or answer[idx + i] != 0:
                        continue

                    answer[idx] = i
                    answer[idx + i] = i
                    visited[i] = True

                    dfs(idx+1)

                    visited[i] = False
                    answer[idx] = 0
                    answer[idx + i] = 0

        dfs(0)
        return result[0]
