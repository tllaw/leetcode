class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        i, j, r = 1, n - 1, 0

        while i < j:
            m, c = (i + j) // 2, 0

            for k in range(n):
                if nums[k] > m:
                    c += 1

            if c <= n - m + 1:
                i = m + 1
            else:
                r = m
                j = m - 1

        return r
