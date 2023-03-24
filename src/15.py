class Solution:
    def threeSum(self, nums):
        nums, n, r = sorted(nums), len(nums), []

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                a = [nums[i], nums[j], nums[k]]
                s = sum(a)

                if s == 0:
                    r.append(a)

                if s <= 0:
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                if s >= 0:
                    k -= 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return r
