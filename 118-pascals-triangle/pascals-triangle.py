class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1 for _ in range(numRows)] for _ in range(numRows)]
        
        for i in range(1, numRows):
            for j in range(i+1,numRows):
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        
        answer = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                temp.append(dp[j][i])
            answer.append(temp)

        return answer