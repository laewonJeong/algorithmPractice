class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        idx_nums = [(num, i) for i, num in enumerate(nums)]
        sort_nums = sorted(idx_nums)
        groups = []
        group_idxs = []
        group = [sort_nums[0][0]]
        group_idx = [sort_nums[0][1]]

        for i in range(1, len(nums)):
            if abs(sort_nums[i-1][0] - sort_nums[i][0]) <= limit:
                group.append(sort_nums[i][0])
                group_idx.append(sort_nums[i][1])
            else:
                group.sort()
                group_idx.sort()
                groups.append(group)
                group_idxs.append(group_idx)
                group = [sort_nums[i][0]]
                group_idx = [sort_nums[i][1]]
        
        group.sort()
        group_idx.sort()
        groups.append(group)
        group_idxs.append(group_idx)

        for group, group_idx in zip(groups, group_idxs):
            for i in range(len(group)):
                nums[group_idx[i]] = group[i]
        
        return nums