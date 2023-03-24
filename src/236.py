class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return self.recursion(root, p, q)[0]

    def recursion(self, root, p, q):
        if not root:
            return (None, 0)

        left  = self.recursion(root.left, p, q)
        right = self.recursion(root.right, p, q)

        if left[0] or right[0]:
            return left if left[0] else right

        found = left[1] + right[1] + (root.val == p.val) + (root.val == q.val)

        return (root if found == 2 else None, found)
