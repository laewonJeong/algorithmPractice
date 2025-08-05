class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        answer = len(fruits)

        for fruit in fruits:
            for i in range(len(baskets)):
                if fruit <= baskets[i]:
                    answer -= 1
                    baskets[i] = -1
                    break

        return answer