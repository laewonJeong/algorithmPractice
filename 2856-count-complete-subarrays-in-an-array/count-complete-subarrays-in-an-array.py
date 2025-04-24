class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct_cnt = len(set(nums))
        answer = 0

        for i in range(n):
            temp = set()
            for j in range(i, n):
                temp.add(nums[j])
                if len(temp) == distinct_cnt:
                    answer += 1
        
        return answer