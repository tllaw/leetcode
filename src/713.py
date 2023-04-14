class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        i, n, p, result = 0, len(nums), 1, 0

        for j in range(n):
            p *= nums[j]

            while i <= j and p >= k:
                p //= nums[i]
                i += 1

            result += j - i + 1

        return result
