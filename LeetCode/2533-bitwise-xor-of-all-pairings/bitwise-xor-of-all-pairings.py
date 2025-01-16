def make_answer(nums, answer, n):
    for num in nums:
        bin_num = bin(num)[2:]
        idx = n - 1
        for i in range(len(bin_num)-1, -1, -1):
            if bin_num[i] == '1':
                if answer[idx] == '1':
                    answer[idx] = '0'
                else:
                    answer[idx] = '1'
            idx-=1

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        max_value = max(max(nums1), max(nums2))
        len_nums1, len_nums2 = len(nums1), len(nums2)
        n = len(bin(max_value))-2
        answer = ['0' for _ in range(n)]

        if len_nums2 % 2 != 0:
            make_answer(nums1, answer, n)

        if len_nums1 % 2 != 0:
            make_answer(nums2, answer, n)
        
        return int(''.join(answer), 2)