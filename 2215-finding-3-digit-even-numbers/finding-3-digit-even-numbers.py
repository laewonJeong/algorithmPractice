class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        answer = []
        for even_num in range(100, 999, 2):
            c = even_num % 10
            b = even_num // 10 % 10
            a = even_num // 100
            list_even_num =[a, b, c]

            check = True
            for digit in list_even_num:
                if list_even_num.count(digit) > digits.count(digit):
                    check = False
                    break
            
            if check:
                answer.append(even_num)
        
        return answer