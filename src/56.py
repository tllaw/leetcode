class Solution:
    def merge(self, intervals):
        intervals, result = sorted(intervals, key=lambda interval: interval[0]), []

        for interval in intervals:
            if len(result) != 0 and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result
