class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        answer = 0
        mod = 10**9 + 7
        odd_count, even_count = 0, 1

        prefix_sum = 0
        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                answer += odd_count
                even_count += 1
            else:
                answer += even_count
                odd_count += 1

        return answer % mod