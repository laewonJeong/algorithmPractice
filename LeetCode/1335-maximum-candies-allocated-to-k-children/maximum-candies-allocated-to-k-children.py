def can_get(candies, k, mid):
    cnt = 0

    for candy in candies:
        cnt += candy//mid

    return cnt >= k

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sum_candies = sum(candies)
        if sum_candies < k:
            return 0

        left, right = 1, sum_candies//k + 1

        while left <= right:
            mid = (left + right) // 2

            if can_get(candies, k, mid):
                left = mid + 1
            else:
                right = mid - 1

        return right