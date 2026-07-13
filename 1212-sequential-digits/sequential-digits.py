class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq_digits = ["12", "23", "34", "45", "56", "67", "78", "89"]
        
        for i in range(1, 8):
            for j in range(8 - i):
                before_digits = seq_digits[len(seq_digits) - (8 - i) - 1]
                seq_digits.append(before_digits + str(int(before_digits[-1]) + 1))


        answer = []

        for digit in seq_digits:
            int_digit = int(digit)
            if int_digit >= low and int_digit <= high:
                answer.append(int_digit)

        return answer