class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        answer = []

        for i in range(n-1, -1, -1):
            if len(answer) < k:
                answer.append(nums[i])
            else:
                min_num = min(answer)
                if nums[i] > min_num:
                    answer.remove(min_num)
                    answer.append(nums[i])
            
        return answer[::-1]
        