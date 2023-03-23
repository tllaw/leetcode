class Solution:
    def combinationSum(self, candidates, target):
        result = []
        nums = sorted(candidates)

        def backtrack(curr, i, target):
            if target <= 0:
                if target == 0:
                    result.append(list(curr))
                return

            for j in range(i, len(nums)):
                curr.append(nums[j])
                target -= nums[j]

                backtrack(curr, j, target)

                curr.pop()
                target += nums[j]

        backtrack([], 0, target)
        return result
