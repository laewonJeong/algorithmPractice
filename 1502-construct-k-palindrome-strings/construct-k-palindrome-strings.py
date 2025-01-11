class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False
            
        s_counter = Counter(s)

        odd_s = []
        
        for alpha in s_counter:
            if s_counter[alpha] % 2 != 0:
                odd_s.append(alpha)

        if len(odd_s) > k:
            return False
        else:
            return True
        
        