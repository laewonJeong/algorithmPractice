class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        sequence = [0] * ((n - 1) * 2 + 1)
        visited = [False] * (n + 1)
        answer = None

        def backtracking(idx):
            nonlocal answer
            if answer:
                return

            if idx == (n - 1) * 2 + 1:
                answer = sequence[:]
                return
            
            if sequence[idx] != 0:
                backtracking(idx + 1)
                return

            for i in range(n, 0, -1):
                if visited[i]:
                    continue
                
                if i == 1:
                    sequence[idx] = i
                    visited[i] = True
                    backtracking(idx + 1)
                    visited[i] = False
                    sequence[idx] = 0
                else:
                    if idx + i >= (n - 1) * 2 + 1 or sequence[idx + i] != 0:
                        continue

                    sequence[idx] = i
                    sequence[idx + i] = i
                    visited[i] = True

                    backtracking(idx + 1)

                    visited[i] = False
                    sequence[idx] = 0
                    sequence[idx + i] = 0

        backtracking(0)
        return answer