class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        temp = [[] for _ in range(n+m-1)]

        for j in range(m):
            idx = j
            for i in range(n):
                temp[idx].append(mat[i][j])
                idx += 1

        answer = []
        for i in range(len(temp)):
            if i % 2 != 0:
                temp[i] = temp[i][::-1]
            for num in temp[i]:
                answer.append(num)

        return answer