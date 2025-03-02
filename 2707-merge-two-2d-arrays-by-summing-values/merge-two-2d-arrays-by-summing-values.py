class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums = nums1 + nums2
        nums.sort()

        n = len(nums)

        i = 0
        answer = []
        while i < n-1:
            if nums[i][0] == nums[i+1][0]:
                answer.append([nums[i][0], nums[i][1] + nums[i+1][1]])
                i+=2
            else:
                answer.append(nums[i])
                i+=1

        if answer[-1][0] != nums[-1][0]:
            answer.append(nums[-1])

        return answer