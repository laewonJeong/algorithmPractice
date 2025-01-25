class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sort_nums = sorted([(num, i) for i, num in enumerate(nums)])
        groups, group_idxs = [], []
        now_group, now_group_idx = [sort_nums[0][0]], [sort_nums[0][1]]

        for i in range(1, n):
            if abs(sort_nums[i-1][0] - sort_nums[i][0]) <= limit:
                now_group.append(sort_nums[i][0])
                now_group_idx.append(sort_nums[i][1])
            else:
                groups.append(sorted(now_group))
                group_idxs.append(sorted(now_group_idx))
                now_group, now_group_idx = [sort_nums[i][0]], [sort_nums[i][1]]
        
        groups.append(sorted(now_group))
        group_idxs.append(sorted(now_group_idx))      

        for group, group_idx in zip(groups, group_idxs):
            for num, idx in zip(group, group_idx):
                nums[idx] = num
        
        return nums