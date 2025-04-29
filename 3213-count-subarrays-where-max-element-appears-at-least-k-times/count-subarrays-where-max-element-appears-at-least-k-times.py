class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        count = 0
        n = len(nums)
        right = 0

        answer = 0
        for left in range(n):
            while right < n and count < k:
                if nums[right] == max_num:
                    count += 1
                right += 1
            
            if count >= k:
                answer += n-right+1
            
            if nums[left] == max_num:
                count -= 1

        return answer
