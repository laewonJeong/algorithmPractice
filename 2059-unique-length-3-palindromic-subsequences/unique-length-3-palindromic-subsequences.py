class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        answer = 0
        check = defaultdict(bool)

        for i in range(n):
            j = n - 1
            left = s[i]
            if not check[left]:
                while s[j] != left:
                    j-=1
                answer += len(set(s[i+1:j]))
            check[left] = True


        return answer