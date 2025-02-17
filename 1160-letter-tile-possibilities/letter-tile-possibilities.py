class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequence = set()
        n = len(tiles)
        visited = [False] * n

        def backtracking(now, now_len, tiles, n):
            nonlocal sequence

            if now:
                sequence.add(''.join(now))
            if now_len == n:
                return
            
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    now.append(tiles[i])
                    
                    backtracking(now, now_len, tiles, n)

                    now.pop()
                    visited[i] = False
        
        backtracking([], 0, tiles, n)

        return len(sequence)