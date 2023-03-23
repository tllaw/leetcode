class Solution:
    def rightSideView(self, root):
        # result = []
        # self.recursion(result, root, 0)
        # return result
        return self.iteration(root)

    def recursion(self, result, root, level):
        if not root:
            return

        if len(result) > level:
            result[level] = root.val
        else:
            result.append(root.val)

        self.recursion(result, root.left, level + 1)
        self.recursion(result, root.right, level + 1)

    def iteration(self, root):
        queue, result = [(root, 0)], []

        while queue:
            el, level = queue.pop(0)

            if not el:
                continue

            queue.extend([(el.left, level + 1), (el.right, level + 1)])

            if len(result) > level:
                result[level] = el.val
            else:
                result.append(el.val)

        return result
