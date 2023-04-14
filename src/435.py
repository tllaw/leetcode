class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda interval: interval[1])
        end, result = -math.inf, 0

        for s, e in intervals:
            if end <= s:
                end = e
            else:
                result += 1

        return result
