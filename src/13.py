class Solution:
    def romanToInt(self, s):
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        r, p = 0, d[s[0]]

        for c in s:
            if d[c] > p:
                r -= p * 2
            r += d[c]
            p = d[c]

        return r
