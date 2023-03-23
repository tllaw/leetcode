class Solution:
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        curr   = 1

        for i in range(len(nums) - 1, 0, -1):
            result[i - 1] = result[i] * nums[i]

        for i in range(len(nums)):
            result[i] *= curr
            curr      *= nums[i]

        return result
