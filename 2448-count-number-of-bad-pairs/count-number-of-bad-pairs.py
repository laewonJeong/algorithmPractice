class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)

        c = defaultdict(int)
        answer = n * (n-1)//2

        for i in range(n):
            c[nums[i] - i] += 1
        
        for k, v in c.items():
            if v > 1:
                answer -= v*(v-1)//2
        
        return answer