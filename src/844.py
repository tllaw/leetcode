class Solution:
    def backspaceCompare(self, s, t):
        i, j, c, d = len(s) - 1, len(t) - 1, 0, 0

        while i >= 0 or j >= 0:
            while i >= 0 and (c or s[i] == '#'):
                c += 1 if s[i] == '#' else -1
                i -= 1

            while j >= 0 and (d or t[j] == '#'):
                d += 1 if t[j] == '#' else -1
                j -= 1

            if ((i >= 0) ^ (j >= 0)) or (i >= 0 and j >= 0 and s[i] != t[j]):
                return False

            i, j = i - 1, j - 1

        return True
