class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        temp = [[] for _ in range(len(mat)*len(mat[0]))]
        n = len(mat)
        m = len(mat[0])

        if n == 1:
            return mat[0]

        for j in range(m):
            idx = j
            for i in range(n):
                temp[idx].append(mat[i][j])
                idx += 1
        
        answer = []
        for i in range(len(temp)):
            if i % 2 == 0:
                for num in temp[i]:
                    answer.append(num)
            else:
                for num in temp[i][::-1]:
                    answer.append(num)
        
        return answer