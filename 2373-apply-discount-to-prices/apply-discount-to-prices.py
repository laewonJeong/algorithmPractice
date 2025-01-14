class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        split_sentence = sentence.split()
        n = len(split_sentence)
        discount = discount / 100
        answer = ""

        for i in range(n):
            ss = split_sentence[i]
            dollor = ss[0]
            money = "".join(ss[1:])
            if dollor == "$" and money.isdigit():
                int_money = int(money)
                split_sentence[i] = f'${(int_money - int_money * discount):.2f}'
            
            answer += split_sentence[i] + ' '
        
        return answer[:-1]