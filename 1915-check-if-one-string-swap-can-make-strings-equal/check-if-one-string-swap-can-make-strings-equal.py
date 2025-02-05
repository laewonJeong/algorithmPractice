class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        
        n = len(s1)
        n = len(s1)
        check_alpha = Counter()
        for i in range(n):
            if s1[i] != s2[i]:
                check_alpha[s1[i]] += 1
                check_alpha[s2[i]] += 1

        if len(check_alpha) == 2 and sum(check_alpha.values()) == 4:
            return True
        else:
            return False
