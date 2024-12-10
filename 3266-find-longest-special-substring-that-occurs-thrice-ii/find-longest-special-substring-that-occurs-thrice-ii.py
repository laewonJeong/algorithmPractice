class Solution:
    def maximumLength(self, s: str) -> int:
        substring_dic = defaultdict(list)
        n = len(s)
        len_substring = [0] * n
        len_substring[0] = 1


        for i in range(1, n):
            if s[i] == s[i-1]:
                len_substring[i] = len_substring[i-1]+1
            else:
                len_substring[i] = 1

        for i in range(n):
            substring_dic[s[i]].append(len_substring[i])
                
        answer = -1
        
        for key in substring_dic:
            if len(substring_dic[key]) >= 3:
                if len(substring_dic[key]) == substring_dic[key].count(1):
                    answer = max(answer, 1)
                else:
                    answer = max(answer,sorted(substring_dic[key])[-3])

        
        return answer