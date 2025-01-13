class Solution:
    def minimumLength(self, s: str) -> int:
        count_s = Counter(s)
        answer = len(s)

        for alpha in count_s:
            if count_s[alpha] > 2:
                if count_s[alpha] % 2 == 1:
                    answer -= (count_s[alpha]) - 1
                else:
                    answer -= (count_s[alpha]) - 2

        return answer