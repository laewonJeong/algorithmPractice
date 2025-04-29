class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        n = len(nums)
        count = 0
        left = 0
        answer = 0

        for right in range(n):
            if nums[right] == max_num:
                count += 1

            while count >= k:
                if nums[left] == max_num:
                    count-=1
                left += 1
            
            answer += left

        return answer
