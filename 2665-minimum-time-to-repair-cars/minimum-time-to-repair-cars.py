class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * cars ** 2

        def can_minute(ranks, cars, mid):
            c = 0
            for rank in ranks:
                c += int(math.isqrt(mid//rank))
                if c >= cars:
                    return True
            return c >= cars

        while left < right:
            mid = (left + right) // 2

            if can_minute(ranks, cars, mid):
                right = mid
            else:
                left = mid + 1

        return right    