class Solution:
    def findMin(self, nums):
        i, j, r = 0, len(nums) - 1, inf

        while i <= j:
            m = (i + j) // 2
            r = min(r, nums[m])

            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m - 1

        return r
