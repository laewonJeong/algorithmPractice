class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        moves = [[0,1], [1,0], [0,-1], [-1,0]]

        q = [(0,0,0)]
        heapq.heapify(q)
        visited = set()
        visited.add((0,0))

        while q:
            time, x, y = heapq.heappop(q)

            if x == n - 1 and y == m - 1:
                return time
            
            for move in moves:
                nx = x+move[0]
                ny = y+move[1]

                if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if moveTime[nx][ny] > time:
                        heapq.heappush(q, (max(time, moveTime[nx][ny]) + 1,nx,ny))
                    else:
                        heapq.heappush(q, (time + 1,nx,ny))