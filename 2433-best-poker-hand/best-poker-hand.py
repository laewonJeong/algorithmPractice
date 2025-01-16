class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        c_ranks = defaultdict(int)
        c_suits = defaultdict(int)
        n = len(ranks)
        max_v = 0


        for i in range(n):
            c_ranks[ranks[i]] += 1
            if c_ranks[ranks[i]] > max_v:
                max_v = c_ranks[ranks[i]]

            c_suits[suits[i]] += 1
            if c_suits[suits[i]] == 5:
                return "Flush"

        if max_v >= 3:
            return "Three of a Kind"
        elif max_v >=2:
            return "Pair"
        else:
            return "High Card"

        