class Solution:
    def missingNumber(self, nums):
        r = len(nums)

        for i, n in enumerate(nums):
            r ^= i ^ n

        return r
