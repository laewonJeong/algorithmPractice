def num_one_count(nums_one, len_num, nums, n):
     for num in nums:
        bin_num = bin(num)
        idx = n-1
        for i in range(len(bin_num)-1, -1, -1):
            if bin_num[i] == 'b':
                break
            elif bin_num[i] == '1':
                nums_one[idx] += 1 * (len_num % 2)
            idx -= 1

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        max_value = max(max(nums1), max(nums2))
        len_nums1, len_nums2 = len(nums1), len(nums2)

        n = len(bin(max_value))-2
        nums1_one = [0 for _ in range(n)]
        nums2_one = [0 for _ in range(n)]

        num_one_count(nums1_one, len_nums2, nums1, n)
        num_one_count(nums2_one, len_nums1, nums2, n)

        answer = ['0' for _ in range(n)]
        for i in range(n):
            if (nums2_one[i] + nums1_one[i]) % 2 == 1:
                answer[i] = '1'
               
        return int(''.join(answer), 2)