class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = deque()
        check_distinct = defaultdict(int)
        answer, now_sum = 0, 0
        len_d, len_cd = 0, 0

        for num in nums:
            d.append(num)
            now_sum += num
            len_d += 1
            check_distinct[num] += 1

            if check_distinct[num] == 1:
                len_cd += 1

            if len_d > k:
                left = d.popleft()
                len_d -= 1
                now_sum -= left
                check_distinct[left] -= 1

                if not check_distinct[left]:
                    check_distinct.pop(left)
                    len_cd -= 1

            if len_cd == k and len_d == k:
                answer = max(answer, now_sum)

        return answer
