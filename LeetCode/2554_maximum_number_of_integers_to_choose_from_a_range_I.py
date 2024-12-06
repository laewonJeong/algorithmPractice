class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        check = defaultdict(bool)
        new_banned = []
        for banned_num in banned:
            if not check[banned_num]:
                new_banned.append(banned_num)
                check[banned_num] = True

        sum_num = 0
        cnt = 0
        for i in range(1, n+1):
            if i not in new_banned:
                sum_num += i
                cnt += 1
            if sum_num > maxSum:
                cnt -= 1
                break
        
        return cnt
