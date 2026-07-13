class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq_digits = ["1","2","3","4","5","6","7","8","9"]
        answer = []

        for i in range(1, 9):
            for _ in range(9 - i):
                before_digits = seq_digits[len(seq_digits) - (9 - i) - 1]
                after_digits = before_digits + str(int(before_digits[-1]) + 1)
                seq_digits.append(after_digits)
                if low <= int(after_digits) <= high:
                    answer.append(int(after_digits))

        return answer