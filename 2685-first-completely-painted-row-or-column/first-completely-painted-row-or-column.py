class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        row = [0 for _ in range(n)]
        col = [0 for _ in range(m)]

        xy = [0 for _ in range(n*m+1)]

        for i in range(n):
            for j in range(m):
                xy[mat[i][j]] = (i, j)

        for i in range(n*m+1):
            x, y = xy[arr[i]]
            row[x] += 1
            col[y] += 1
            if row[x] == m or col[y] == n:
                return i