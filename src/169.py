class Solution:
    def majorityElement(self, nums):
        m, r = {}, nums[0]

        for n in nums:
            m[n] = m.get(n, 0) + 1
            if m[n] > m[r]:
                r = n

        return r
