class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count_s = Counter(s)
        alpha = sorted(count_s.keys(), reverse = True)
        n = len(alpha)

        answer = ""

        for i in range(n):
            check_limit = 0
            current_alpha = alpha[i]

            while count_s[current_alpha] != 0:
                answer += current_alpha
                count_s[current_alpha] -= 1
                check_limit+=1

                if check_limit == repeatLimit and count_s[current_alpha] > 0:
                    for j in range(i+1, n):
                        next_alpha = alpha[j]

                        if count_s[next_alpha] != 0:
                            answer += next_alpha
                            count_s[next_alpha] -= 1
                            break
                            
                    if answer[-1] == current_alpha:
                        break

                    check_limit = 0
        
        return answer
