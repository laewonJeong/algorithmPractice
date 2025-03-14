class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        left, right = 1, max(candies)

        def can_get(candies, k, mid):
            cnt = 0

            for candy in candies:
                if candy >= mid:
                    cnt += candy//mid

            return cnt >= k

        while left <= right:
            mid = (left + right) // 2

            if can_get(candies, k, mid):
                left = mid + 1
            else:
                right = mid - 1


        return left-1