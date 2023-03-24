class Solution:
    def searchRange(self, nums, target):
        n, r = len(nums), [-1, -1]
        i, j = 0, n - 1

        while i <= j:
            m = (i + j) // 2

            if nums[m] >= target:
                if nums[m] == target:
                    r[0] = m
                j = m - 1
            else:
                i = m + 1

        i, j = 0, n - 1

        while i <= j:
            m = (i + j) // 2

            if nums[m] <= target:
                if nums[m] == target:
                    r[1] = m
                i = m + 1
            else:
                j = m - 1

        return r
