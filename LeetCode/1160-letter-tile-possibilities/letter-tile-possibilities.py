class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        answer = 0
        sequence = set()
        n = len(tiles)
        visited = [False] * n

        def backtracking(now, tiles, n, visited):
            nonlocal answer
            if now:
                sequence.add(''.join(now))
                answer += 1
            
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    now.append(tiles[i])

                    if ''.join(now) not in sequence:
                        backtracking(now, tiles, n, visited)

                    now.pop()
                    visited[i] = False
        
        backtracking([], tiles, n, visited)

        return answer