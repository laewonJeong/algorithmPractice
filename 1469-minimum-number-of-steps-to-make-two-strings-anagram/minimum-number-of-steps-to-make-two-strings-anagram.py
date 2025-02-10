class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        common_alpha_count = count_s & count_t

        if common_alpha_count == count_s:
            return 0

        answer = 0
        for alpha in count_s:
            if alpha in common_alpha_count:
                answer += count_s[alpha] - common_alpha_count[alpha]
            else:
                answer += count_s[alpha]
        
        return answer