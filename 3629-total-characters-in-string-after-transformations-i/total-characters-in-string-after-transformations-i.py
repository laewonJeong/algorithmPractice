class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7
        count = defaultdict(int)
        for c in s:
            count[ord(c) - 97] += 1
        
        for _ in range(t):
            new_count = defaultdict(int)
            for i in range(26):
                if i == 25:
                    new_count[0] = (new_count[0] + count[25]) % mod
                    new_count[1] = (new_count[1] + count[25]) % mod
                else:
                    new_count[i + 1] = (new_count[i + 1] + count[i]) % mod
            count = new_count
        
        return sum(count.values()) % mod
