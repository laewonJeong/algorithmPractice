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
            for num in temp[i][::i%2*-2+1]:
                answer.append(num)

        return answer