class Solution:  
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 1:
            if abs(target) == abs(nums[0]):
                return 1
            else:
                return 0

        answer = 0
        set_list = [set() for i in range(n)]
        set_list[0].add(nums[0])
        count = [defaultdict(int) for i in range(n)]

        for i in range(1, n):
            for j in set_list[i-1]:
                if count[i-1][j] > 0:
                    count[i][j+nums[i]] += count[i-1][j]
                    count[i][j-nums[i]] += count[i-1][j]
                else:
                    count[i][j+nums[i]] += 1
                    count[i][j-nums[i]] += 1
                set_list[i].add(j + nums[i])
                set_list[i].add(j - nums[i])

        return count[-1][target] + count[-1][-target]