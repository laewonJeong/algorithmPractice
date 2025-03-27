class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        nums_counter = Counter(nums)
        cnt, max_num = max((v, k) for k, v in nums_counter.items())

        left_cnt = 0
        right_cnt = cnt
        for i, num in enumerate(nums):
            if num == max_num:
                left_cnt += 1
                right_cnt -= 1

                if left_cnt * 2 > i + 1 and right_cnt * 2 > n-i-1:
                    return i

        return -1
            
            