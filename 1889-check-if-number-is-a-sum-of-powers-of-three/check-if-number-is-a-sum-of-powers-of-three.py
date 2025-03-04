class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        check_sum = []

        for i in range(16):
            three_power = 3 ** i

            if three_power < n:
                check_sum.append(three_power)
                
                for j in range(len(check_sum)-1):
                    sum_power_of_three = check_sum[j] + three_power

                    if sum_power_of_three == n:
                        return True

                    elif sum_power_of_three < n:
                        check_sum.append(sum_power_of_three)
            
            else:
                return three_power == n