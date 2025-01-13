class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        elif (s[0] == ')' and locked[0] == '1') or (s[-1] =='(' and locked[-1] == '1'):
            return False

        n = len(s)
        lock = []
        no_lock = []

        for i in range(n):
            if s[i] == '(' and locked[i] == '1':
                lock.append(s[i])
            elif locked[i] == '0':
                no_lock.append(s[i])
            else:
                if lock:
                    lock.pop()
                elif no_lock:
                    no_lock.pop()
                else:
                    return False

        lock = []
        no_lock = []

        for i in range(n-1, -1, -1):
            if s[i] == ')' and locked[i] == '1':
                lock.append(s[i])
            elif locked[i] == '0':
                no_lock.append(s[i])
            else:
                if lock:
                    lock.pop()
                elif no_lock:
                    no_lock.pop()
                else:
                    return False
    
        return True