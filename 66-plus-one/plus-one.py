class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digit = int(''.join(str(i) for i in digits))
            digit += 1
            return list(map(int, str(digit)))