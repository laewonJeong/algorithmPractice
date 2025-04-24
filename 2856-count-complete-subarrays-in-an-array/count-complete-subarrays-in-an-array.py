class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct_cnt = len(set(nums))
        answer, left = 0, 0
        num_cnt = defaultdict(int)

        for right in range(n):
            num_cnt[nums[right]] += 1

            while len(num_cnt) == distinct_cnt:
                answer += n - right
                num_cnt[nums[left]] -= 1
                if num_cnt[nums[left]] == 0:
                    del num_cnt[nums[left]]
                left += 1
        
        return answer