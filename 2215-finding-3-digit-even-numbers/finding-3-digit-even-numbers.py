class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        answer = []
        for even_num in range(100, 999, 2):
            list_even_num = list(map(int, str(even_num)))

            check = True
            for digit in list_even_num:
                if list_even_num.count(digit) > digits.count(digit):
                    check = False
                    break
            
            if check:
                answer.append(even_num)
        
        return answer