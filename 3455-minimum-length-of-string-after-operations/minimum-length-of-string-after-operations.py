class Solution:
    def minimumLength(self, s: str) -> int:
        count_s = Counter(s)
        answer = len(s)

        for alpha in count_s:
            while count_s[alpha] > 2:
                count_s[alpha] -= 2
                answer -=2
        
        return answer