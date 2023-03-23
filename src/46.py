class Solution:
    def permute(self, nums):
        result = []

        def backtrack(curr):
            if nums == []:
                result.append(list(curr))
                return

            for i in range(len(nums)):
                curr.append(nums.pop(i))
                backtrack(curr)
                nums.insert(i, curr.pop())

        backtrack([])
        return result
