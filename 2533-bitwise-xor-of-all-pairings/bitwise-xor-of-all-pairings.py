class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        max_value = max(max(nums1), max(nums2))
        len_nums1, len_nums2 = len(nums1), len(nums2)

        n = len(bin(max_value))-2
        nums1_one = [0 for _ in range(n)]
        nums2_one = [0 for _ in range(n)]

        for num in nums1:
            bin_num = bin(num)
            idx = n-1
            for i in range(len(bin_num)-1, -1, -1):
                if bin_num[i] == 'b':
                    break
                elif bin_num[i] == '1':
                    nums1_one[idx] += 1 * len_nums2
                idx -= 1

        for num in nums2:
            bin_num = bin(num)
            idx = n-1
            for i in range(len(bin_num)-1, -1, -1):
                if bin_num[i] == 'b':
                    break
                elif bin_num[i] == '1':
                    nums2_one[idx] += 1 * len_nums1
                idx -= 1

        answer = ""
        for i in range(n):
            if (nums2_one[i] + nums1_one[i]) % 2 == 1:
                answer += "1"
            else:
                answer += "0"

        return int(answer,2)