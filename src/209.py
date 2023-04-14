class Solution:
    def minSubArrayLen(self, target, nums):
        i, n, s, result = 0, len(nums), 0, math.inf

        for j in range(n):
            s += nums[j]

            while i <= j and s >= target:
                result = min(j - i + 1, result)
                s -= nums[i]
                i += 1

        return result if result != math.inf else 0
