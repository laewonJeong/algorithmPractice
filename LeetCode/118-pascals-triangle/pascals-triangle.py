class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1 for _ in range(numRows)] for _ in range(numRows)]
        answer = [[1]]
        
        for i in range(1, numRows):
            temp = [1]
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                temp.append(dp[i][j])
            temp.append(1)
            answer.append(temp)

        return answer

        #1
        #1 1
        #1 2 1
        #1 3 3 1
        #1 4 6 4 1