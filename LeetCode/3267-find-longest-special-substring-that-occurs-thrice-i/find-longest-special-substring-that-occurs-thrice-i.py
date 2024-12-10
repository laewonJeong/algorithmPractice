class Solution:
    def maximumLength(self, s: str) -> int:
        substring_dic = defaultdict(int)
        n = len(s)

        for i in range(n):
            j = i+1
            substring_dic[s[i]] += 1
            temp = s[i]

            while True:
                if j == n or s[i] != s[j]:
                    break
                temp += s[j]
                substring_dic[temp] += 1
                j+=1
                
        answer = -1

        for substring in substring_dic:
            if substring_dic[substring] >= 3:
                answer = max(answer, len(substring))
        
        return answer