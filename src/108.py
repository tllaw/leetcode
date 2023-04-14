class Solution:
    def sortedArrayToBST(self, nums, head=0, tail=-math.inf):
        if tail == -math.inf:
            tail = len(nums) - 1

        if head > tail:
            return None

        mid   = head + (tail - head) // 2
        left  = self.sortedArrayToBST(nums, head, mid - 1)
        right = self.sortedArrayToBST(nums, mid + 1, tail)

        return TreeNode(nums[mid], left, right)
