class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        max_a = max(A)
        max_b = max(B)
        check = [0 for _ in range(max(max_a, max_b)+1)]

        answer = []
        temp = 0
        for num_a, num_b in zip(A, B):
            check[num_a] += 1
            if check[num_a] == 2:
                temp += 1
                
            check[num_b] += 1
            if check[num_b] == 2:
                temp += 1
            answer.append(temp)
            
        return answer