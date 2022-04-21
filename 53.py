class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        maximum, current = nums[0], 0

        for n in nums:
            current = max(current, 0) + n
            maximum = max(maximum, current)

        return maximum
