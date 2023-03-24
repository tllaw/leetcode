class Solution:
    def findPeakElement(self, nums):
        i, j = 0, len(nums) - 1

        while i < j:
            m = (i + j) // 2

            if nums[m] > nums[m + 1]:
                j = m
            else:
                i = m + 1

        return i
