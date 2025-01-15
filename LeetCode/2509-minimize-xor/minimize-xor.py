def change_bin_num1(bin_num1, need, f, t):
    for i in range(len(bin_num1)-1, -1, -1):
        if need == 0:
            break
        elif bin_num1[i] == f:
            bin_num1[i] = t
            need -=1

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bin_num1 = list(bin(num1)[2:])
        bin_num2 = list(bin(num2)[2:])

        if len(bin_num2) > len(bin_num1):
            bin_num1 = ['0'] * (len(bin_num2) - len(bin_num1)) + bin_num1
        else:
            bin_num2 = ['0'] * (len(bin_num1) - len(bin_num2)) + bin_num2

        num1_one = bin_num1.count('1')
        num2_one = bin_num2.count('1')

        if num1_one == num2_one:
            return num1
        elif num1_one < num2_one:
            need = num2_one - num1_one
            change_bin_num1(bin_num1, need, '0', '1')
        else:
            need = num1_one - num2_one
            change_bin_num1(bin_num1, need, '1', '0')

        return int(''.join(bin_num1), 2)