def make_powers(n):
    result = []
    k = 0
    while n > 0:
        if n % 2 == 1:
            result.append(int(pow(2, k)))
        n //= 2
        k += 1
    return result

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        answer = []
        powers = make_powers(n)
        
        
        for i in range(1, len(powers)):
            powers[i] = powers[i] * powers[i-1]

        print(powers)
        for a, b in queries:
            if a == 0:
                answer.append(powers[b] % (10**9 + 7))
            else:
                answer.append(powers[b] // powers[a-1] % (10**9 + 7))
        
        return answer