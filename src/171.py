class Solution:
    def titleToNumber(self, columnTitle):
        r = 0

        for c in columnTitle:
            r = r * 26 + (ord(c) - ord("A") + 1)

        return r
