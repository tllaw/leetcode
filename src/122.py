class Solution:
    def maxProfit(self, prices):
        r, c = 0, prices[0]

        for p in prices:
            if p > c:
                r += p - c
            c = p

        return r
