class Solution:
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        random.shuffle(nums)

        def recursion(head, tail):
            i = head

            for j in range(head, tail):
                if nums[j] < nums[tail]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[tail] = nums[tail], nums[i]

            if i == k:
                return nums[i]

            if i < k:
                return recursion(i + 1, tail)
            else:
                return recursion(head, i - 1)


        return recursion(0, len(nums) - 1)
