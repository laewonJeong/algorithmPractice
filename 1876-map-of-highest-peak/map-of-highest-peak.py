class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        answer = [[-1 for _ in range(m)] for _ in range(n)]

        q = deque([])
        visited = defaultdict(bool)

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    answer[i][j] = 0
        
        moves = [[0, 1], [0, -1], [1, 0], [-1,0]]

        while q:
            x, y = q.popleft()

            for move in moves:
                nx = x + move[0]
                ny = y + move[1]

                if 0<= nx < n and 0 <= ny < m and answer[nx][ny] == -1:
                    answer[nx][ny] = answer[x][y] + 1
                    q.append((nx, ny))
        
        return answer