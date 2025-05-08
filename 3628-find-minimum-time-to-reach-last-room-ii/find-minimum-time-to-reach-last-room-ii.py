class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        moves = [[0,1], [1,0], [0,-1], [-1,0]]

        q = [(0,0,0,1)]
        heapq.heapify(q)
        visited = set()
        visited.add((0,0))

        while q:
            time, x, y, second = heapq.heappop(q)

            if x == n - 1 and y == m - 1:
                return time
            
            for move in moves:
                nx = x+move[0]
                ny = y+move[1]

                if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    temp = 1 if second == 2 else 2
                    if moveTime[nx][ny] > time:
                        heapq.heappush(q, (moveTime[nx][ny] + second,nx,ny, temp))
                    else:
                        heapq.heappush(q, (time + second,nx,ny, temp))