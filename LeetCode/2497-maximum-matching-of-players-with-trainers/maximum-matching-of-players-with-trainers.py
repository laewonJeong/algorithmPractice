class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse = True)
        trainers.sort(reverse = True)
        n = len(trainers)

        answer = 0
        trainers_idx = 0

        for player in players:
            if trainers_idx < n and player <= trainers[trainers_idx]:
                answer+=1
                trainers_idx+=1
        
        return answer
