class Solution:
    def sortColors(self, nums):
        i, n = 0, len(nums)

        for j in range(n):
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        for j in range(i, n):
            if nums[j] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
