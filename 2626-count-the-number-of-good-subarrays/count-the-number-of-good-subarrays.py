class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dup, right = 0, -1
        cnt = defaultdict(int)
        ans = 0
        for left in range(n):
            while dup < k and right + 1 < n:
                right += 1
                dup += cnt[nums[right]]
                cnt[nums[right]] += 1
            if dup >= k:
                ans += n-right
            cnt[nums[left]] -= 1
            dup -= cnt[nums[left]]
        return ans