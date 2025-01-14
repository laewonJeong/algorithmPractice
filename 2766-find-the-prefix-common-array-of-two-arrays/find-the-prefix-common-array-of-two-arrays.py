class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        check_a = Counter()
        check_b = Counter()

        answer = []

        for num_a, num_b in zip(A, B):
            check_a[num_a] += 1
            check_b[num_b] += 1

            answer.append(list((check_a + check_b).values()).count(2))

        return answer