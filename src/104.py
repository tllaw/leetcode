class Solution:
    def maxDepth(self, root, curr = 0):
        if not root:
            return curr

        left  = self.maxDepth(root.left, curr + 1)
        right = self.maxDepth(root.right, curr + 1)
        return max(left, right)
