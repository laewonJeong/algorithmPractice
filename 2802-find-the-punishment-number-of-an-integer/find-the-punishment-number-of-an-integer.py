class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0
        
        @lru_cache(None)
        def partition(i, now, target, string):
            if i == len(string) and now == target:
                return True

            for j in range(i, len(string)):
                if partition(j + 1, now + int(string[i:j+1]), target, string):
                    return True
            return False

        for i in range(1, n + 1):
            if partition(0, 0, i, str(i * i)):
                result += i * i 
        
        return result