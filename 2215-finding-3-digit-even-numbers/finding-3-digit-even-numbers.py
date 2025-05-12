class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        answer = []
        digit_counter = Counter(digits)

        for even_num in range(100, 999, 2):
            c = even_num % 10
            b = even_num // 10 % 10
            a = even_num // 100
            digit_counter[a] -= 1
            digit_counter[b] -= 1
            digit_counter[c] -= 1

            if all(digit_counter[i] >= 0 for i in [a,b,c]):
                answer.append(even_num)
            
            digit_counter[a] += 1
            digit_counter[b] += 1
            digit_counter[c] += 1

        return answer
