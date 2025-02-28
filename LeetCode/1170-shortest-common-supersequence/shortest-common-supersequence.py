class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif str1[j-1] == str2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        #for d in dp:
        #    print(d)
        q = deque([(m,n)])

        sub_sequence = ''
        while q:
            x, y = q.popleft()
            if dp[x][y] == 0:
                break

            if dp[x-1][y] != dp[x][y] and dp[x][y-1] != dp[x][y]:
                sub_sequence += str2[x-1]
                q.append((x-1, y-1))
            elif dp[x-1][y] == dp[x][y]:
                q.append((x-1,y))
            elif dp[x][y-1] == dp[x][y]:
                q.append((x, y-1))

        sub_sequence = sub_sequence[::-1]
        
        answer = ''
        i, j = 0, 0
        for ss in sub_sequence:
            while ss != str1[i]:
                answer += str1[i]
                i+=1
            while ss != str2[j]:
                answer += str2[j]
                j+=1
            
            answer += ss
            i+=1
            j+=1
        
        answer += str1[i:] + str2[j:]

        return answer
        