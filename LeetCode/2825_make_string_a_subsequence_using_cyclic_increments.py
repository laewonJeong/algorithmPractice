class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        n1 = len(str1)
        n2 = len(str2)

        while i != n1 and j != n2:
            next_alpha = chr(ord(str1[i])+1) if str1[i] != 'z' else 'a'
            if str1[i] == str2[j] or next_alpha == str2[j]:
                j += 1
            i+=1

        if j == n2:
            return True
        return False
