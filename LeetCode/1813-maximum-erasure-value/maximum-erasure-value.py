class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique = [False] * (10**4+1)
        answer = 0
        sub_sum = 0
        right = 0
        n = len(nums)

        temp = []
        for left in range(n):
            while right < n and not unique[nums[right]]:
                sub_sum += nums[right]
                unique[nums[right]] = True
                right+=1
            
            answer = max(answer, sub_sum)
            unique[nums[left]] = False
            sub_sum -= nums[left]

        return answer
