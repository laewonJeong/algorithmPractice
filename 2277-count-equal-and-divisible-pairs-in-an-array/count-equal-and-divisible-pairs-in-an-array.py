class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        n = len(nums)
        answer = 0

        for i in range(n):
            dic[nums[i]].append(i)
        
        for v in dic.values():
            for comb in tuple(combinations(v, 2)):
                if comb[0] * comb[1] % k == 0:
                    answer += 1
        
        return answer