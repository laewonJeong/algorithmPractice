class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        count = defaultdict(int)
        n = len(nums)
        right = 0

        answer = 0
        for left in range(n):
            while right < n and count[max_num] < k:
                count[nums[right]] += 1
                right += 1
            
            if count[max_num] >= k:
                answer += n-right+1
            count[nums[left]] -= 1

        return answer
