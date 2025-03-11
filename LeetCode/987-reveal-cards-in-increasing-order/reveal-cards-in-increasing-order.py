class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        d = deque(range(len(deck)))
        answer = [0] * len(deck)

        for card in deck:
            answer[d.popleft()] = card
            if d:
                d.append(d.popleft())

        return answer
