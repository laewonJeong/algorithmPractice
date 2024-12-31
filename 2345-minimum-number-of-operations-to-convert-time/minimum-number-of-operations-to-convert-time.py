def change_to_minute(time):
    time = time.split(':')
    return int(time[0]) * 60 + int(time[1])

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current == correct:
            return 0

        answer = 0
        current = change_to_minute(current)
        correct = change_to_minute(correct)

        while current != correct:
            if current + 60 <= correct:
                current += 60
            elif current + 15 <= correct:
                current += 15
            elif current + 5 <= correct:
                current += 5
            else:
                current += 1
            
            answer += 1

        return answer
        