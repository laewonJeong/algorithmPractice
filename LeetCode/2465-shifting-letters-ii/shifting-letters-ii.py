class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        total_shift = [0 for _ in range(len(s)+1)]
        
        for start, end, d in shifts:
            if d == 1:
                total_shift[start] += 1
                total_shift[end+1] -= 1
            else:
                total_shift[start] -= 1
                total_shift[end+1] += 1
        
        for i in range(len(s)):
            if i > 0:
                total_shift[i] += total_shift[i-1]

            shift_alpha = ord(s[i]) + (total_shift[i] % 26)

            if shift_alpha > ord('z'):
                shift_alpha -= 26
            elif shift_alpha < ord('a'):
                shift_alpha += 26

            s[i] = chr(shift_alpha)

        return ''.join(s)