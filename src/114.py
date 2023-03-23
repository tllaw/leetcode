class Solution:
    def flatten(self, root):
        # self.recursion(root)
        self.iteration(root)

    def recursion(self, root):
        if not root:
            return root

        left, right = self.dfs(root.left), self.dfs(root.right)
        root.left = None
        root.right = left

        curr = root
        while curr.right:
            curr = curr.right
        curr.right = right

        return root

    def iteration(self, root):
        stack, tail = [root], TreeNode()

        while stack:
            curr = stack.pop()

            if not curr:
                continue

            stack.extend([curr.right, curr.left])
            curr.left = None
            tail.right = curr
            tail = tail.right
