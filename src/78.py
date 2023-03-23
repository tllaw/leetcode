class Solution:
    def subsets(self, nums):
        # return self.cascading(nums)
        # return self.backtrack(nums)
        return self.bitmask(nums)

    def cascading(self, nums):
        result = [[]]

        for n in nums:
            result += [el + [n] for el in result]

        return result

    def backtrack(self, nums):
        result = []

        def backtrack(length, head, curr):
            if len(curr) == length:
                result.append(list(curr))
                return

            for i in range(head, len(nums)):
                curr.append(nums[i])
                backtrack(length, i + 1, curr)
                curr.pop()

        for length in range(len(nums) + 1):
            backtrack(length, 0, [])

        return result

    def bitmask(self, nums):
        n = len(nums)
        result = []

        for i in range(2 ** n, 2 ** (n + 1)):
            mask = bin(i)[3:]
            result.append([nums[j] for j in range(n) if mask[j] == '1'])

        return result
