class Solution:
    def invertTree(self, root):
        # return self.recursive(root)
        return self.iterative(root)

    def recursive(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(self, root.left)
            self.invertTree(self, root.right)
        return root

    def iterative(self, root):
        if not root:
            return root

        queue = [root]

        while len(queue):
            el = queue.pop()
            el.left, el.right = el.right, el.left

            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)

        return root
