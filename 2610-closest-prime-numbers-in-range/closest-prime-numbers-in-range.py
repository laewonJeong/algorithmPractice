class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def make_prime_num(n):
            prime = [True] * (n+1)
            prime[0] = False
            if n > 0:
                prime[1] = False
            for i in range(2, int(math.sqrt(n)) + 1):
                if prime[i]:
                    j=2
                    for j in range(i * i, n + 1, i):
                        prime[j] = False

            return [i for i in range(left, right + 1) if prime[i]]

        prime = make_prime_num(right)

        if len(prime) < 2:
            return [-1, -1]
        
        answer = [left-1, right+1]
        for i in range(len(prime)-1):
            if prime[i+1] - prime[i] < answer[1] - answer[0]:
                answer[0] = prime[i]
                answer[1] = prime[i+1] 

        return answer