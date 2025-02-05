class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        
        n = len(s1)
        check_diff = 0
        for i in range(n):
            if s1[i] != s2[i]:
                check_diff += 1

        if check_diff == 2:
            return True
        else:
            return False
