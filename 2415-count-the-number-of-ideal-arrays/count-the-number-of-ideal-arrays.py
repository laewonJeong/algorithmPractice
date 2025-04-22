class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        answer = maxValue
        freq_map = {num: 1 for num in range(1, maxValue + 1)}
        
        for arr_size in range(1, n): 
            new_freq = Counter()
            for base_val in freq_map: 
                for multiplier in range(2, maxValue // base_val + 1): 
                    combinations = comb(n - 1, arr_size)
                    answer += combinations * freq_map[base_val]
                    new_freq[multiplier * base_val] += freq_map[base_val]
            freq_map = new_freq
            answer %= MOD
        
        return answer 