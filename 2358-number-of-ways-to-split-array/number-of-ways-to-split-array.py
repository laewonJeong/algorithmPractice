class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] + nums[i]

        for i in range(n-1):
            if prefix[i] >= suffix[i+1]:
                answer += 1
        
        return answer